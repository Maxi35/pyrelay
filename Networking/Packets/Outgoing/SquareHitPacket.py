class SquareHitPacket:
    def __init__(self):
        self.type = "SQUAREHIT"
        self.time = 0
        self.bulletId = 0
        self.objectId = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeByte(self.bulletId)
        writer.writeInt32(self.objectId)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readByte()
        self.objectId = reader.readInt32()
