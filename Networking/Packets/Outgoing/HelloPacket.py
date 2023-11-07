class HelloPacket:
    def __init__(self):
        self.type = "HELLO"
        self.send = True
        self.gameId = 0
        self.buildVersion = ""
        self.accessToken = ""
        self.keyTime = 0
        self.key = []
        self.userPlatform = ""
        self.playPlatform = ""
        self.platformToken = ""
        self.userToken = ""
        self.token = "fRT6i7Zqv6e1GyCRb6EMAT58a6YI1MWc"

    def write(self, writer):
        writer.writeInt32(self.gameId)
        writer.writeStr(self.buildVersion)
        writer.writeStr(self.accessToken)
        writer.writeInt32(self.keyTime)
        writer.writeBytes(self.key)
        writer.writeStr(self.userPlatform)
        writer.writeStr(self.playPlatform)
        writer.writeStr(self.platformToken)
        writer.writeStr(self.userToken)
        writer.writeStr(self.token)

    def read(self, reader):
        self.gameId = reader.readInt32()
        self.buildVersion = reader.readStr()
        self.accessToken = reader.readStr()
        self.keyTime = reader.readInt32()
        self.key = reader.readBytes()
        self.userPlatform = reader.readStr()
        self.playPlatform = reader.readStr()
        self.platformToken = reader.readStr()
        self.userToken = reader.readStr()
        self.token = reader.readStr()
