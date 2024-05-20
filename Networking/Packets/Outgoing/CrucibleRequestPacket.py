from Networking.Packets.Packet import Packet

class CrucibleRequestPacket(Packet):
    def __init__(self):
        self.type = "CRUCIBLEREQUEST"
        self.unknownShort = 0
        self.unknownInt1 = 0
        self.unknownInt2 = 0

    def write(self, writer):
        writer.writeShort(self.unknownShort)
        writer.writeInt32(self.unknownInt1)
        writer.writeInt32(self.unknownInt2)

    def read(self, reader):
        self.unknownShort = reader.readShort()
        self.unknownInt1 = reader.readInt32()
        self.unknownInt2 = reader.readInt32()
