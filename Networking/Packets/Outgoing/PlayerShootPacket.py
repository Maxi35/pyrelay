from Networking.Packets.Packet import Packet
from Data.WorldPosData import *

class PlayerShootPacket(Packet):
    def __init__(self):
        self.type = "PLAYERSHOOT"
        self.time = 0
        self.shotId = 0
        self.containerType = 0
        self.bulletId = 0#-1 if the weapon doesn't have a bullet type
        self.shotPos = WorldPosData()
        self.angle = 0
        self.burstId = 0#Out of max nubmer of bursts
        self.unknownShort = -256
        self.pos = WorldPosData()

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.shotId)
        writer.writeShort(self.containerType)
        writer.writeByte(self.bulletId)
        self.shotPos.write(writer)
        writer.writeFloat(self.angle)
        writer.writeByte(self.burstId)
        writer.writeShort(self.unknownShort)
        self.pos.write(writer)

    def read(self, reader):
        self.time = reader.readInt32()
        self.shotId = reader.readShort()
        self.containerType = reader.readShort()
        self.bulletId = reader.readByte()
        self.shotPos.read(reader)
        self.angle = reader.readFloat()
        self.burstId = reader.readByte()
        self.unknownShort = reader.readShort()
        self.pos.read(reader)
