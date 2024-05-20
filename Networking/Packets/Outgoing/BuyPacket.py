from Networking.Packets.Packet import Packet

class BuyPacket(Packet):
    def __init__(self):
        self.type = "BUY"
        self.objectId = 0
        self.quantity = 0

    def write(self, writer):
        writer.writeInt32(self.objectId)
        writer.writeInt32(self.quantity)

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.quantity = reader.readInt32()
