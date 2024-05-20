from Networking.Packets.Packet import Packet

class CancelTradePacket(Packet):
    def __init__(self):
        self.type = "CANCELTRADE"
        self.objectId = 0

    def write(self, writer):
        pass

    def read(self, reader):
        pass
