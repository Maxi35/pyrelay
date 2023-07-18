from Data.WorldPosData import *

class PlayerShootPacket:
    def __init__(self):
        self.type = "PLAYERSHOOT"
        self.send = True
        self.time = 0
        self.bulletId = 0
        self.containerType = 0
        self.unknownByte = 0
        self.pos = WorldPosData()
        self.angle = 0
        self.isBurst = False
        self.unknownShort = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeShort(self.containerType)
        writer.writeByte(self.unknownByte)
        self.pos.write(writer)
        writer.writeFloat(self.angle)
        writer.writeBool(self.isBurst)
        writer.writeShort(self.unknownShort)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.containerType = reader.readShort()
        self.unknownByte = reader.readByte()
        self.pos.read(reader)
        self.angle = reader.readFloat()
        self.isBurst = reader.readBool()
        self.unknownShort = reader.readShort()
