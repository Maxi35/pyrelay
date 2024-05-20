from Networking.Packets.Packet import Packet

class EnemyHitPacket(Packet):
    def __init__(self):
        self.type = "ENEMYHIT"
        self.time = 0
        self.bulletId = 0
        self.id1 = 0
        self.targetId = 0
        self.kill = False
        self.id2 = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeInt32(self.id1)
        writer.writeInt32(self.targetId)
        writer.writeBool(self.kill)
        writer.writeInt32(self.id2)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.id1 = reader.readInt32()
        self.targetId = reader.readInt32()
        self.kill = reader.readBool()
        self.id2 = reader.readInt32()
