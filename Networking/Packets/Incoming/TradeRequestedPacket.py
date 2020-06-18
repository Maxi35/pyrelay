class TradeRequestedPacket:
    def __init__(self):
        self.type = "TRADEREQUESTED"
        self.name = ""

    def read(self, reader):
        self.name = reader.readStr()
