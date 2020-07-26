import random

class HelloPacket:
    def __init__(self):
        self.type = "HELLO"
        self.buildVersion = ""
        self.gameId = 0
        self.guid = ""
        self.random1 = int(random.random()*1000000000)
        self.password = ""
        self.random2 = int(random.random()*1000000000)
        self.secret = ""
        self.keyTime = 0
        self.key = []
        self.mapJSON = ""
        self.entryTag = ""
        self.gameNet = ""
        self.gameNetUserId = ""
        self.playPlatform = ""
        self.platformToken = ""
        self.userToken = ""
        self.token = "8bV53M5ysJdVjU4M97fh2g7BnPXhefnc"
        self.previousConnectionGuid = ""

        self.legacyToken = "XTeP7hERdchV5jrBZEYNebAqDPU6tKU6"

    def write(self, writer):
        writer.writeStr(self.buildVersion)
        writer.writeInt32(self.gameId)
        writer.writeStr(self.guid)
        writer.writeInt32(self.random1)
        writer.writeStr(self.password)
        writer.writeInt32(self.random2)
        writer.writeStr(self.secret)
        writer.writeInt32(self.keyTime)
        writer.writeBytes(self.key)
        writer.writeStr32(self.mapJSON)
        writer.writeStr(self.entryTag)
        writer.writeStr(self.gameNet)
        writer.writeStr(self.gameNetUserId)
        writer.writeStr(self.playPlatform)
        writer.writeStr(self.platformToken)
        writer.writeStr(self.userToken)
        writer.writeStr(self.token)
        writer.writeStr(self.previousConnectionGuid)
