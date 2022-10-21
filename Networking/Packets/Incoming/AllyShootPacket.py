class AllyShootPacket:
    def __init__(self):
        self.type = "ALLYSHOOT"
        self.bulletId = 0
        self.ownerId = []
        self.containerType = 0
        self.angle = 0
        self.bard = False

    def read(self, reader):
        self.bulletId = reader.readUnsignedShort()
        self.ownerId = reader.readInt32()
        self.containerType = reader.readShort()
        self.angle = reader.readFloat()
        self.bard = reader.readBool()

    def write(self, writer):
        writer.writeUnsignedShort(self.bulletId)
        writer.writeInt32(self.ownerId)
        writer.writeShort(self.containerType)
        writer.writeFloat(self.angle)
        writer.writeBool(self.bard)
