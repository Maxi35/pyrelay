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
        self.bulletId = reader.readUnsignedShort()
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

    def writer(self, writer):
        writer.writeUnsignedShort(self.bulletId)
        writer.writeInt32(self.ownerId)
        writer.writeUnsignedByte(self.bulletType)
        self.startingPos.write(writer)
        writer.writeFloat(self.angle)
        writer.writeShort(self.damage)
        if self.angleInc == 0 and self.numShots == 1:
            writer.writeUnsignedByte(self.numShots)
            writer.writeFloat(self.angleInc)
        else:
            self.numShots = 1
            self.angleInc = 0
