class CancelTradePacket:
    def __init__(self):
        self.type = "CANCELTRADE"
        self.objectId = 0

    def write(self, writer):
        pass
