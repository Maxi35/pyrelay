from Networking.Packets.Packet import Packet

class EnemyShootAckPacket(Packet):
    def __init__(self):
        self.type = "ENEMYSHOOTACK"
        self.time = 0
        self.count = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.count)

    def read(self, reader):
        self.time = reader.readInt32()
        self.count = reader.readShort()
