from Data.WorldPosData import *

class PlayerShootPacket:
    def __init__(self):
        self.type = "PLAYERSHOOT"
        self.time = 0
        self.bulletId = 0
        self.containerType = 0
        self.pos = WorldPosData()
        self.angle = 0
        self.speedMult = 0
        self.lifeMult = 0
        self.isBurst = False

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeShort(self.containerType)
        self.pos.write(writer)
        writer.writeFloat(self.angle)
        writer.writeShort(int(self.speedMult*1000))
        writer.writeShort(int(self.lifeMult*1000))
        writer.writeBool(self.isBurst)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.containerType = reader.readShort()
        self.pos.read(reader)
        self.angle = reader.readFloat()
        self.speedMult = int(reader.readShort()/1000)
        self.lifeMult = int(reader.readShort()/1000)
        self.isBurst = reader.readBool()
