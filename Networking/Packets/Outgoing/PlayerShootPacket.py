from Networking.Packets.Packet import Packet
from Data.WorldPosData import *

class PlayerShootPacket(Packet):
    def __init__(self):
        self.type = "PLAYERSHOOT"
        self.time = 0
        self.bulletId = 0
        self.containerType = 0
        self.unknownByte = 0
        self.shotPos = WorldPosData()
        self.angle = 0
        self.isBurst = False
        self.unknownShort = 0
        self.pos = WorldPosData()

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.bulletId)
        writer.writeShort(self.containerType)
        writer.writeByte(self.unknownByte)
        self.shotPos.write(writer)
        writer.writeFloat(self.angle)
        writer.writeBool(self.isBurst)
        writer.writeShort(self.unknownShort)
        self.pos.write(writer)

    def read(self, reader):
        self.time = reader.readInt32()
        self.bulletId = reader.readShort()
        self.containerType = reader.readShort()
        self.unknownByte = reader.readByte()
        self.shotPos.read(reader)
        self.angle = reader.readFloat()
        self.isBurst = reader.readBool()
        self.unknownShort = reader.readShort()
        self.pos.read(reader)
