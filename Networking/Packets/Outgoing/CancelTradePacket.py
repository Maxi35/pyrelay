class CancelTradePacket:
    def __init__(self):
        self.type = "CANCELTRADE"
        self.send = True
        self.objectId = 0

    def write(self, writer):
        pass

    def read(self, reader):
        pass
