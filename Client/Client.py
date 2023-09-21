import time
import math
import threading
import requests
import urllib.parse
import hashlib
import re

from Helpers.Random import Random
from Networking.SocketManager import SocketManager
from Models.PlayerData import PlayerData
from Models.CharData import CharData
import Helpers.Servers as ServersHelper
import Data.MoveRecord as MoveRecord
import Models.ConditionEffect as ConditionEffect
import Networking.PacketHelper as PacketHelper
import Constants.GameIds as GameId
import Constants.Servers as Servers
import Constants.ApiPoints as ApiPoints
import Constants.ClassIds as Classes
import Crypto.RSA as RSA

MINSPEED = 0.004
MAXSPEED = 0.0096

MINFREQ = 0.0015
MAXFREQ = 0.008

class Client:
    def __init__(self):
        self.guid = ""
        self.password = ""
        self.secret = ""
        self.alias = ""
        self.server = ""
        self.proxy = {}
        self.internalServer = {"host": "", "name": ""}
        self.nexusServer = {"host": "", "name": ""}
        self.pos = None
        self.sockMan = None
        self.clientManager = None
        self.anyPacket = None
        self.nextPos = []
        self.objectId = -1
        self.connectedTime = -1
        self.random = Random()
        self.frameTimeUpdater = None
        self.active = True
        self.isReady = False
        self.key = []
        self.keyTime = -1
        self.connectionGuid = ""
        self.gameId = GameId.nexus
        self.buildVersion = open("gameVersion.txt").read()
        self.clientToken = ""
        self.accessToken = ""
        self.playerData = PlayerData()
        self.charData = CharData()
        self.needsNewChar = False
        self.bulletId = 0
        self.lastAttackTime = 0

    def getToken(self, accInfo, updateServers=False):
        self.guid = accInfo["guid"]
        self.password = accInfo["password"]
        self.secret = accInfo["secret"]
        self.alias = accInfo["alias"]
        self.proxy = accInfo.get("proxy", {})

        proxies = {}
        if self.proxy != {}:
            proxies = {
                "https": "socks{}://".format(self.proxy["type"]) +
                ("{}:{}@".format(self.proxy["username"], self.proxy["password"]) if self.proxy["username"] != "" else "") +
                "{}:{}".format(self.proxy["host"], self.proxy["port"])
                }
        self.clientToken = hashlib.md5(self.guid.encode("utf-8") + self.password.encode("utf-8")).hexdigest()
        print("Getting token...")
        #Get access token
        r = requests.post(ApiPoints.VERIFY, data={"guid": self.guid,
                                                  "password": self.password,
                                                  "clientToken": self.clientToken,
                                                  "game_net": "Unity", "play_platform": "Unity", "game_net_user_id": ""}, headers=ApiPoints.launcherHeaders, proxies=proxies)
        pattern = r"AccessToken>(.+)</AccessToken>"
        try:
            self.accessToken = re.findall(pattern, r.text)[0]
        except IndexError:#Token not working
            print("GETTING TOKEN ERROR:", r.text)
            self.active = False
            return
        #Verify token
        r = requests.post(ApiPoints.VERIFYTOKEN, data={"clientToken": self.clientToken,
                                                       "accessToken": self.accessToken,
                                                       "game_net": "Unity", "play_platform": "Unity", "game_net_user_id": ""}, headers=ApiPoints.launcherHeaders, proxies=proxies)
        if not "Success" in r.text:
            print("VERIFYING TOKEN ERROR:", r.text)
            self.active = False
            return
            
        #Get char data
        r = requests.post(ApiPoints.CHAR, data={"do_login": "true",
                                                "accessToken": self.accessToken,
                                                "game_net": "Unity", "play_platform": "Unity", "game_net_user_id": ""}, headers=ApiPoints.launcherHeaders, proxies=proxies)
        while "Account in use" in r.text:
            print(self.guid, "has account in use")
            try:
                time.sleep(int(re.findall(r"(\d+)", r.text)[0]))
            except IndexError:
                time.sleep(600)
            r = requests.post(ApiPoints.CHAR, data={"do_login": "true",
                                                    "accessToken": self.accessToken,
                                                    "game_net": "Unity", "play_platform": "Unity", "game_net_user_id": ""}, headers=ApiPoints.launcherHeaders, proxies=proxies)
        if "Account credentials not valid" in r.text:
            print(self.guid, "got invalid credentials")
            self.active = False
            return
        try:
            charInfo = re.findall(r'<Chars nextCharId="(\d+)" maxNumChars="(\d+)">', r.text)[0]
            chars = re.findall(r'<Char id="(\d+)">', r.text)
        except IndexError:
            print(r.text)
            self.active = False
            return
        self.charData.nextCharId = int(charInfo[0])
        self.charData.maxNumChars = int(charInfo[1])
        if len(chars) > 0:
            self.charData.charIds = [int(i) for i in chars]
            self.charData.currentCharId = int(chars[0])
        else:
            self.charData.charIds = [self.charData.nextCharId]
            self.charData.currentCharId = self.charData.nextCharId
            self.charData.nextCharId += 1
            self.needsNewChar = True
            
        self.isReady = True

        try:
            if updateServers:
                ServersHelper.update(self.accessToken, proxies)
                print("Updated servers")
        except AttributeError as e:
            print("Failed to update servers")
            print(e)
            self.active = False
            self.isReady = False

    def setup(self, accInfo):
        self.server = accInfo["server"]
        self.connectedTime = int(time.time()*1000)
        
        self.internalServer = {"host": Servers.nameToIp[self.server],
                               "name": self.server}
        self.nexusServer = {"host": Servers.nameToIp[self.server],
                            "name": self.server}
        
        self.sockMan = SocketManager()
        self.sockMan.hook("ANY", self.onPacket)
        self.anyPacket = None
        
        self.sockMan.hook("CREATESUCCESS", self.onCreateSuccess)
        self.sockMan.hook("ENEMYSHOOT", self.onEnemyShoot)
        self.sockMan.hook("FAILURE", self.onFailure)
        self.sockMan.hook("GOTO", self.onGoto)
        self.sockMan.hook("MAPINFO", self.onMapInfo)
        self.sockMan.hook("NEWTICK", self.onNewTick)
        self.sockMan.hook("PING", self.onPing)
        self.sockMan.hook("UPDATE", self.onUpdate)
        self.sockMan.hook("RECONNECT", self.onReconnect)
        self.sockMan.hook("SERVERPLAYERSHOOT", self.onServerPlayerShoot)
    
    def isConnected(self):
        return self.sockMan.connected

    def connect(self):
        if not self.active:
            return
        if self.sockMan.connected:
            self.sockMan.disconnect()
        if not self.frameTimeUpdater is None:
            self.frameTimeUpdater.cancel()
        self.sockMan.connect(self.internalServer["host"], self.proxy)
        self.sendHelloPacket()

    def changeServer(self, server):
        if not server in Servers.nameToIp.keys():
            print(server, "is not a valid server")
            return
        self.server = server
        self.internalServer = {"host": Servers.nameToIp[self.server],
                               "name": self.server}
        self.nexusServer = {"host": Servers.nameToIp[self.server],
                            "name": self.server}
        self.connect()

    def getSpeed(self, time):
        if self.hasEffect(ConditionEffect.SLOWED):
            return MINSPEED
        speed = MINSPEED + (self.playerData.spd+self.playerData.spdBoost)/75 * (MAXSPEED-MINSPEED)
        if self.hasEffect(ConditionEffect.SPEEDY, ConditionEffect.NINJASPEEDY):
            speed *= 1.5
        return speed * time
    
    def nexus(self):
        packet = PacketHelper.CreatePacket("ESCAPE")
        self.send(packet)
        self.gameId = GameId.nexus
        self.key = []
        self.keyTime = -1

    def sendHelloPacket(self):
        hello_packet = PacketHelper.CreatePacket("HELLO")
        hello_packet.buildVersion = self.buildVersion
        hello_packet.gameId = self.gameId
        hello_packet.accessToken = self.accessToken
        hello_packet.keyTime = self.keyTime
        hello_packet.key = self.key
        hello_packet.gameNet = "rotmg"
        hello_packet.playPlatform = "rotmg"
        hello_packet.userToken = self.clientToken
        self.send(hello_packet)

    def send(self, packet):
        if self.isConnected():
            self.sockMan.sendPacket(packet)

    def getTime(self):
        return int(time.time()*1000) - self.connectedTime

    def disconnect(self):
        self.active = False
        if self.sockMan.connected:
            self.sockMan.disconnect()
        self.sockMan.active = False
        if not self.frameTimeUpdater is None:
            self.frameTimeUpdater.cancel()

    def updateFrameTime(self):
        time = self.getTime()
        delta = time - self.lastFrameTime
        if len(self.nextPos) > 0:
            diff = min(33, time-self.lastFrameTime)
            self.moveTo(self.nextPos[0], diff)
        self.lastFrameTime = time
        self.frameTimeUpdater = threading.Timer(1/30, self.updateFrameTime)
        self.frameTimeUpdater.daemon = True
        self.frameTimeUpdater.start()

    def moveTo(self, target, time):
        speed = self.getSpeed(time)
        if self.pos.dist(target) > speed:
            angle = math.atan2(target.y-self.pos.y, target.x-self.pos.x)
            self.walkTo(self.pos + (math.cos(angle) * speed, math.sin(angle) * speed))
        else:
            self.walkTo(target)
            self.nextPos.pop(0)

    def walkTo(self, target):
        if self.hasEffect(ConditionEffect.PARALYZED, ConditionEffect.PAUSED, ConditionEffect.PETRIFIED):
            return
        self.pos = target.clone()

    def attackFreq(self):
        if self.hasEffect(ConditionEffect.DAZED):
            return MINFREQ
        freq = MINFREQ + (self.playerData.dex+self.playerData.dexBoost)/75 * (MAXFREQ - MINFREQ)
        if self.hasEffect(ConditionEffect.BERSERK):
            freq *= 1.5
        return freq

    def getBulletId(self):
        bulletId = self.bulletId
        self.bulletId = (self.bulletId + 1) % 128
        return bulletId

    def shoot(self, angle):
        if self.clientManager.weapons is None:
            print("Weapons not loaded")
            return False
        if self.hasEffect(ConditionEffect.STUNNED, ConditionEffect.PAUSED, ConditionEffect.PETRIFIED):
            return False
        if not self.playerData.inv[0] in self.clientManager.weapons.keys():
            return False
        time = self.getTime()
        attackPeriod = 1 / self.attackFreq() * (1/1)#TODO
        if time < self.lastAttackTime + attackPeriod:
            return False
        self.lastAttackTime = time

        shootPacket = PacketHelper.CreatePacket("PLAYERSHOOT")
        shootPacket.time = time
        shootPacket.containerType = self.playerData.inv[0]
        shootPacket.speedMult = self.playerData.projSpeedMult
        shootPacket.lifeMult = self.playerData.projLifeMult

        weapon = self.clientManager.weapons[shootPacket.containerType]
        arcRads = weapon.arcGap * math.pi / 180
        totalArc = arcRads * (weapon.numProjectiles - 1)
        if totalArc < 0:
            totalArc = 0
        angle -= totalArc/2

        for i in range(weapon.numProjectiles):
            shootPacket.bulletId = self.getBulletId()
            shootPacket.pos = self.pos.clone()
            shootPacket.pos.x += math.cos(angle) * 0.3
            shootPacket.pos.y += math.sin(angle) * 0.3
            shootPacket.angle = angle
            if arcRads > 0:
                angle += arcRads
            self.send(shootPacket)
            
        return True

    def hasEffect(self, *effects):
        return ConditionEffect.hasEffect(self.playerData.condition, *effects)
    
    def onCreateSuccess(self, packet):
        self.objectId = packet.objectId
        self.lastAttackTime = 0
        self.lastFrameTime = self.getTime()
        self.frameTimeUpdater = threading.Timer(1/30, self.updateFrameTime)
        self.frameTimeUpdater.daemon = True
        self.frameTimeUpdater.start()
    
    def onGoto(self, packet):
        gotoAck_packet = PacketHelper.CreatePacket("GOTOACK")
        gotoAck_packet.time = self.lastFrameTime
        self.send(gotoAck_packet)
        if packet.objectId == self.objectId:
            self.pos = packet.pos.clone()
        
    def onMapInfo(self, packet):
        print("Connected to", self.nexusServer["name"], packet.name)
        if self.needsNewChar:
            print("Creating new char")
            create_packet = PacketHelper.CreatePacket("CREATE")
            create_packet.classType = Classes.WIZARD
            create_packet.skinType = 0
            create_packet.isChallenger = 0
            self.send(create_packet)
            self.needsNewChar = False
        else:
            load_packet = PacketHelper.CreatePacket("LOAD")
            load_packet.charId = self.charData.currentCharId
            self.send(load_packet)
        self.random.setSeed(packet.seed)

        show_packet = PacketHelper.CreatePacket("SHOWALLYSHOOT")
        show_packet.toggle = 1
        self.send(show_packet)

    def onFailure(self, packet):
        print("Error:", packet.errorId)
        print(packet.errorDescription)
        if packet.errorDescription == "s.update_client":
            self.disconnect()
        elif packet.errorDescription == "Account credentials not valid":
            self.disconnect()
        elif packet.errorDescription == "Bad message received":
            self.disconnect()
        
    def onPing(self, packet):
        pong_packet = PacketHelper.CreatePacket("PONG")
        pong_packet.serial = packet.serial
        pong_packet.time = self.getTime()
        self.send(pong_packet)

    def onNewTick(self, packet):
        move_packet = PacketHelper.CreatePacket("MOVE")
        move_packet.tickId = packet.tickId
        move_packet.time = packet.serverRealTimeMS
        move_packet.records = [MoveRecord.MoveRecord(self.lastFrameTime, self.pos.x, self.pos.y)]
        self.send(move_packet)
        for status in packet.statuses:
            if status.objectId == self.objectId:
                self.playerData.parseStats(status.stats)

    def onUpdate(self, packet):
        if packet.pos.x != 0.0 and packet.pos.y != 0.0:
            self.pos = packet.pos
        updateAck_packet = PacketHelper.CreatePacket("UPDATEACK")
        self.send(updateAck_packet)
        for obj in packet.newObjs:
            if obj.status.objectId == self.objectId:
                self.pos = obj.status.pos
                self.playerData.parse(obj)

    def onServerPlayerShoot(self, packet):
        if packet.ownerId == self.objectId:
            shootAck = PacketHelper.CreatePacket("SHOOTACK")
            shootAck.time = self.lastFrameTime
            self.send(shootAck)

    def onEnemyShoot(self, packet):
        shootAck = PacketHelper.CreatePacket("SHOOTACK")
        shootAck.time = self.lastFrameTime
        self.send(shootAck)

    def onReconnect(self, packet):
        if packet.host != "":
            self.internalServer["host"] = packet.host
        if packet.name != "":
            self.internalServer["name"] = packet.name
        self.gameId = packet.gameId
        self.key = packet.key
        self.keyTime = packet.keyTime
        self.connect()

    def hookAllPackets(self, func):
        self.anyPacket = func

    def onPacket(self, packet):
        if self.anyPacket is None:
            return
        daemon_thread = threading.Thread(target=self.anyPacket, args=(self, packet,))
        daemon_thread.daemon = True
        daemon_thread.start()
