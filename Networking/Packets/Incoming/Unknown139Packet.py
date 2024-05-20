from Networking.Packets.Packet import Packet

class Unknown139Packet(Packet):
    def __init__(self):
        self.type = "UNKNOWN139"
        self.unknownByte1 = 0
        self.unknownByte2 = 0
        self.unknownByte3 = 0
        self.unknownInt1 = 0
        self.unknownInt2 = 0
        self.byte3 = False

    def read(self, reader):
        self.unknownByte1 = reader.readByte()
        self.unknownByte2 = reader.readByte()
        if reader.bytesAvailable() == 9:
            self.unknownByte3 = reader.readByte()
            self.byte3 = True
        self.unknownInt1 = reader.readInt32()
        self.unknownInt2 = reader.readInt32()

    def write(self, writer):
        writer.writeByte(self.unknownByte1)
        writer.writeByte(self.unknownByte2)
        if self.byte3:
            writer.writeByte(self.unknownByte3)
        writer.writeInt32(self.unknownInt1)
        writer.writeInt32(self.unknownInt2)
