from Networking.Packets.Packet import Packet

class EnemyShootAckPacket(Packet):
    def __init__(self):
        self.type = "ENEMYSHOOTACK"
        self.time = 0
        self.numEnemies = 0#How many enemies shot since last ack

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.numEnemies)

    def read(self, reader):
        self.time = reader.readInt32()
        self.numEnemies = reader.readShort()
