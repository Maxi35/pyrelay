
class EnemyHitPacket:
    """ Sent when a projectile from you or a close-by player hits an enemy """
    def __init__(self):
        self.type = "ENEMYHIT"
        self.time: int = 0  # int32
        self.bulletId: int = 0  # int16
        self.targetId: int = 0  # int32
        self.ownerId: int = 0  # int32
        self.killed: bool = False  # bool
        self.projectileOwnerId: int = 0  # int32

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeInt32(self.targetId)
        writer.writeInt32(self.ownerId)
        writer.writeBool(self.killed)
        writer.writeInt32(self.projectileOwnerId)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.targetId = reader.readInt32()
        self.ownerId = reader.readInt32()
        self.killed = reader.readBool()
        self.projectileOwnerId = reader.readInt32()
