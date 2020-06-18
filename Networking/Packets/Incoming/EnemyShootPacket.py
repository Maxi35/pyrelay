from Data.WorldPosData import *

class EnemyShootPacket:
    def __init__(self):
        self.type = "ENEMYSHOOT"
        self.bulletId = 0
        self.ownerId = 0
        self.bulletType = 0
        self.startingPos = WorldPosData()
        self.angle = 0
        self.damage = 0
        self.numShots = 0
        self.angleInc = 0

    def read(self, reader):
        self.bulletId = reader.readUnsignedByte
        self.ownerId = reader.readInt32()
        self.bulletType = reader.readUnsignedByte()
        self.startingPos.read(reader)
        self.angle = reader.readFloat()
        self.damage = reader.readShort()
        if (reader.bytesAvailable() > 0):
            self.numShots = reader.readUnsignedByte()
            self.angleInc = reader.readFloat()
        else:
            self.numShots = 1
            self.angleInc = 0
