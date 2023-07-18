class OtherHitPacket:
    def __init__(self):
        self.type = "OTHERHIT"
        self.send = True
        self.time = 0
        self.bulletId = 0
        self.objectId = 0
        self.targetId = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeInt32(self.objectId)
        writer.writeInt32(self.targetId)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.objectId = reader.readInt32()
        self.targetId = reader.readInt32()
