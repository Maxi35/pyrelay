class ReconnectPacket:
    def __init__(self):
        self.type = "RECONNECT"
        self.name = ""
        self.host = ""
        self.stats = ""
        self.port = 0
        self.gameId = 0
        self.keyTime = 0
        self.isFromArena = False
        self.key = []

    def read(self, reader):
        self.name = reader.readStr()
        self.host = reader.readStr()
        self.stats = reader.readStr()
        self.port = reader.readInt32()
        self.gameId = reader.readInt32()
        self.keyTime = reader.readInt32()
        self.isFromArena = reader.readBool()
        self.key = reader.readBytes()
