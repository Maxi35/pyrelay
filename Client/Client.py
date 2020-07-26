import time
import math
import threading
import requests
import re

from Helpers.Random import Random
from Networking.SocketManager import SocketManager
from Models.PlayerData import PlayerData
from Models.CharData import CharData
import Models.ConditionEffect as ConditionEffect
import Networking.PacketHelper as PacketHelper
import Constants.GameIds as GameId
import Constants.Servers as Servers
import Constants.ApiPoints as ApiPoints
import Constants.ClassIds as Classes
import Crypto.RSA as RSA

MINSPEED = 0.004
MAXSPEED = 0.0096

class Client:
    def __init__(self, accInfo):
        self.guid = accInfo["guid"]
        self.password = accInfo["password"]
        self.alias = accInfo["alias"]
        self.server = accInfo["server"]
        self.pos = None
        self.nextPos = []
        self.objectId = -1
        self.connectedTime = int(time.time()*1000)
        self.random = Random()
        self.frameTimeUpdater = None
        self.key = []
        self.keyTime = -1
        self.connectionGuid = ""
        self.gameId = GameId.nexus
        self.buildVersion = "1.0.0.0."#TODO
        self.playerData = PlayerData()
        self.charData = CharData()
        self.needsNewChar = False
        self.internalServer = {"host": Servers.nameToIp[self.server],
                               "name": self.server}
        self.nexusServer = {"host": Servers.nameToIp[self.server],
                            "name": self.server}
        
        self.sockMan = SocketManager(self.internalServer["host"])
        self.sockMan.hook("ANY", self.onPacket)
        self.anyPacket = None
        
        self.sockMan.hook("MAPINFO", self.onMapInfo)
        self.sockMan.hook("FAILURE", self.onFailure)
        self.sockMan.hook("PING", self.onPing)
        self.sockMan.hook("UPDATE", self.onUpdate)
        self.sockMan.hook("CREATESUCCESS", self.onCreateSuccess)
        self.sockMan.hook("NEWTICK", self.onNewTick)
        self.sockMan.hook("GOTO", self.onGoto)
        self.sockMan.hook("RECONNECT", self.onReconnect)

        r = requests.get(ApiPoints.CHAR.format(self.guid, self.password))
        while "Account in use" in r.text:
            print(self.guid, "has account in use")
            try:
                time.sleep(int(re.findall(r"(\d+)", r.text)[0]))
                r = requests.get(ApiPoints.CHAR.format(self.guid, self.password))
            except IndexError:
                time.sleep(600)
                r = requests.get(ApiPoints.CHAR.format(self.guid, self.password))
        if "Account credentials not valid" in r.text:
            print(self.guid, "got invalid credentials")
            return
        try:
            charInfo = re.findall(r'<Chars nextCharId="(\d+)" maxNumChars="(\d+)">', r.text)[0]
            chars = re.findall(r'<Char id="(\d+)">', r.text)
        except IndexError:
            print(r.text)
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
        
        self.connect()

    def isConnected(self):
        return self.sockMan.connected

    def connect(self):
        if self.sockMan.connected:
            self.sockMan.disconnect()
        if not self.frameTimeUpdater is None:
            self.frameTimeUpdater.cancel()
        self.sockMan.connect()      
        self.sendHelloPacket()

    def changeGameId(self, gameId):
        print("Changing game id directly doesn't work anymore")
        return
##        print("Changing gameId to", gameId)
##        self.gameId = gameId
##        self.connect()

    def getSpeed(self, time):
        if ConditionEffect.hasEffect(self.playerData.condition, ConditionEffect.SLOWED):
            return MINSPEED
        speed = MINSPEED + (self.playerData.spd+self.playerData.spdBoost)/75 * (MAXSPEED-MINSPEED)
        if ConditionEffect.hasEffect(self.playerData.condition, ConditionEffect.SPEEDY, ConditionEffect.NINJASPEEDY):
            speed *= 1.5
        return speed * time
    
    def nexus(self):
        packet = PacketHelper.CreatePacket("ESCAPE")
        self.send(packet)

    def sendHelloPacket(self):
        hello_packet = PacketHelper.CreatePacket("HELLO")
        hello_packet.buildVersion = self.buildVersion
        hello_packet.gameId = self.gameId
        hello_packet.guid = RSA.encrypt(self.guid)
        hello_packet.password = RSA.encrypt(self.password)
        hello_packet.secret = ""
        hello_packet.keyTime = self.keyTime
        hello_packet.key = self.key
        hello_packet.gameNet = "rotmg"
        hello_packet.playPlatform = "rotmg"
        hello_packet.previousConnectionGuid = self.connectionGuid
        self.send(hello_packet)

    def send(self, packet):
        if self.isConnected():
            self.sockMan.sendPacket(packet)

    def getTime(self):
        return int(time.time()*1000) - self.connectedTime

    def disconnect(self):
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
        self.frameTimeUpdater.deamon = True
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
        if ConditionEffect.hasEffect(self.playerData.condition, ConditionEffect.PARALYZED, ConditionEffect.PAUSED, ConditionEffect.PETRIFIED):
            return
        self.pos = target.clone()
    
    def onCreateSuccess(self, packet):
        self.objectId = packet.objectId
        self.lastFrameTime = self.getTime()
        self.frameTimeUpdater = threading.Timer(1/30, self.updateFrameTime)
        self.frameTimeUpdater.deamon = True
        self.frameTimeUpdater.start()
    
    def onGoto(self, packet):
        gotoAck_packet = PacketHelper.CreatePacket("GOTOACK")
        gotoAck_packet.time = self.lastFrameTime
        self.send(gotoAck_packet)
        if packet.objectId == self.objectId:
            self.pos = packet.pos.clone()
        
    def onMapInfo(self, packet):
        print("Connected to", self.internalServer["name"], packet.name)
        if self.needsNewChar:
            print("Creating new char")
            create_packet = PacketHelper.CreatePacket("CREATE")
            create_packet.classType = Classes.WIZARD
            create_packet.skinType = 0
            self.send(create_packet)
            self.needsNewChar = False
        else:
            load_packet = PacketHelper.CreatePacket("LOAD")
            load_packet.charId = self.charData.currentCharId
            self.send(load_packet)
        self.connectionGuid = packet.connectionGuid
        self.random.setSeed(packet.fp)

    def onFailure(self, packet):
        print("Error:", packet.errorId, "at", packet.errorPlace)
        print(packet.errorDescription)
        
    def onPing(self, packet):
        pong_packet = PacketHelper.CreatePacket("PONG")
        pong_packet.serial = packet.serial
        pong_packet.time = self.getTime()
        self.send(pong_packet)

    def onNewTick(self, packet):
        move_packet = PacketHelper.CreatePacket("MOVE")
        move_packet.tickId = packet.tickId
        move_packet.time = self.lastFrameTime
        move_packet.serverRealTimeMS = packet.serverRealTimeMS
        move_packet.newPos = self.pos
        move_packet.records = []
        self.send(move_packet)
        for status in packet.statuses:
            if status.objectId == self.objectId:
                self.playerData.parseStats(status.stats)

    def onUpdate(self, packet):
        updateAck_packet = PacketHelper.CreatePacket("UPDATEACK")
        self.send(updateAck_packet)
        for obj in packet.newObjs:
            if obj.status.objectId == self.objectId:
                self.pos = obj.status.pos
                self.playerData.parse(obj)

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
        deamon_thread = threading.Thread(target=self.anyPacket, args=(self, packet,))
        deamon_thread.deamon = True
        deamon_thread.start()
