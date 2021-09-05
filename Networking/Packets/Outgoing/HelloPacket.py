import random

class HelloPacket:
    def __init__(self):
        self.type = "HELLO"
        self.buildVersion = ""
        self.gameId = 0
        self.accessToken = ""
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
        
##        self.previousConnectionGuid = ""
##        self.legacyToken = "XTeP7hERdchV5jrBZEYNebAqDPU6tKU6"

    def write(self, writer):
        writer.writeStr(self.buildVersion)
        writer.writeInt32(self.gameId)
        writer.writeStr(self.accessToken)
        writer.writeInt32(self.keyTime)
        writer.writeBytes(self.key)
##        writer.writeStr32(self.mapJSON)
        writer.writeStr(self.entryTag)
        writer.writeStr(self.gameNet)
        writer.writeStr(self.gameNetUserId)
        writer.writeStr(self.playPlatform)
        writer.writeStr(self.platformToken)
        writer.writeStr(self.userToken)
        writer.writeStr(self.token)

    def read(self, reader):
        self.buildVersion = reader.readStr()
        self.gameId = reader.readInt32()
        self.accessToken = reader.readStr()
        self.keyTime = reader.readInt32()
        self.key = reader.readBytes()
##        self.mapJSON = reader.readStr32()
        self.entryTag = reader.readStr()
        self.gameNet = reader.readStr()
        self.gameNetUserId = reader.readStr()
        self.playPlatform = reader.readStr()
        self.platformToken = reader.readStr()
        self.userToken = reader.readStr()
        self.token = reader.readStr()
