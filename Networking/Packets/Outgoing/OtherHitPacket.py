class OtherHitPacket:
    def __init__(self):
        self.type = "OTHERHIT"
        self.time = 0
        self.bulletId = 0
        self.objectId = 0
        self.targetId = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeByte(self.bulletId)
        writer.writeInt32(self.objectId)
        writer.writeInt32(self.targetId)
