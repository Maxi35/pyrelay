class TradeDonePacket:
    def __init__(self):
        self.type = "TRADEDONE"
        self.send = True
        self.code = 0
        self.description = ""

    def read(self, reader):
        self.code = reader.readInt32()
        self.description = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.code)
        writer.writeStr(self.description)
