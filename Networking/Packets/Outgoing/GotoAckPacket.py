class GotoAckPacket:
    def __init__(self):
        self.type = "GOTOACK"
        self.send = True
        self.time = 0
        self.unknownByte = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeByte(self.unknownByte)

    def read(self, reader):
        self.time = reader.readInt32()
        self.unknownByte = reader.readByte()
