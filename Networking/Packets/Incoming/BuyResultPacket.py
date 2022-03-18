class BuyResultPacket:
    def __init__(self):
        self.type = "BUYRESULT"
        self.result = 0
        self.resultString = ""

    def read(self, reader):
        self.result = reader.readInt32()
        self.resultString = reader.readStr()
