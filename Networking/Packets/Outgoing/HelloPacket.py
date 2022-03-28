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
        self.userPlatform = ""
        self.playPlatform = ""
        self.platformToken = ""
        self.userToken = ""
        self.token = "8bV53M5ysJdVjU4M97fh2g7BnPXhefnc"

    def write(self, writer):
        writer.writeStr(self.buildVersion)
        writer.writeInt32(self.gameId)
        writer.writeStr(self.accessToken)
        writer.writeInt32(self.keyTime)
        writer.writeBytes(self.key)
        writer.writeStr(self.userPlatform)
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
        self.userPlatform = reader.readStr()
        self.playPlatform = reader.readStr()
        self.platformToken = reader.readStr()
        self.userToken = reader.readStr()
        self.token = reader.readStr()
