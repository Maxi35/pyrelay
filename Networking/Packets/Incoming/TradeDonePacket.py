class TradeDonePacket:
    def __init__(self):
        self.type = "TRADEDONE"
        self.code = 0
        self.description = ""

    def read(self, reader):
        self.code = reader.readInt32()
        self.description = reader.readStr()
