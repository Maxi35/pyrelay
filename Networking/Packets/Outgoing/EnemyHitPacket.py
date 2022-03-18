class EnemyHitPacket:
    def __init__(self):
        self.type = "ENEMYHIT"
        self.time = 0
        self.bulletId = 0
        self.targetId = 0
        self.kill = False

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeInt32(self.targetId)
        writer.writeBool(self.kill)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.targetId = reader.readInt32()
        self.kill = reader.readBool()
