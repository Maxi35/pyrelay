from Networking.Packets.Packet import Packet

class GotoAckPacket(Packet):
    def __init__(self):
        self.type = "GOTOACK"
        self.time = 0
        self.unknownByte = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeByte(self.unknownByte)

    def read(self, reader):
        self.time = reader.readInt32()
        self.unknownByte = reader.readByte()
