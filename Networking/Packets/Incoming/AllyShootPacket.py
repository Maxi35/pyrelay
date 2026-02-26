from Networking.Packets.Packet import Packet

class AllyShootPacket(Packet):
    def __init__(self):
        self.type = "ALLYSHOOT"
        self.bulletId = 0
        self.ownerId = []
        self.containerType = 0
        self.unknownByte = 0
        self.angle = 0
        self.unknownShort = 0

    def read(self, reader):
        self.bulletId = reader.readUnsignedShort()
        self.ownerId = reader.readInt32()
        self.containerType = reader.readShort()
        self.unknownByte = reader.readByte()
        self.angle = reader.readFloat()
        self.unknownShort = reader.readShort()

    def write(self, writer):
        writer.writeUnsignedShort(self.bulletId)
        writer.writeInt32(self.ownerId)
        writer.writeShort(self.containerType)
        writer.writeByte(self.unknownByte)
        writer.writeFloat(self.angle)
        writer.writeShort(self.unknownShort)
