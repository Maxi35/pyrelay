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

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeByte(self.bulletId)
        writer.writeShort(self.containerType)
        self.pos.write(writer)
        writer.writeFloat(self.angle)
        writer.writeShort(int(self.speedMult*1000))
        writer.writeShort(int(self.lifeMult*1000))
