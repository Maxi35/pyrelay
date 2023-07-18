from Data.WorldPosData import *

class AoePacket:
    def __init__(self):
        self.type = "AOE"
        self.send = True
        self.pos = WorldPosData()
        self.radius = 0
        self.damage = 0
        self.effect = 0
        self.duration = 0
        self.origType = 0
        self.color = 0
        self.armorPierce = False

    def read(self, reader):
        self.pos.read(reader)
        self.radius = reader.readFloat()
        self.damage = reader.readUnsignedShort()
        self.effect = reader.readUnsignedByte()
        self.duration = reader.readFloat()
        self.origType = reader.readUnsignedShort()
        self.color = reader.readInt32()
        self.armorPierce = reader.readBool()
        
    def write(self, writer):
        self.pos.write(writer)
        writer.writeFloat(self.radius)
        writer.writeUnsignedShort(self.damage)
        writer.writeUnsignedByte(self.effect)
        writer.writeFloat(self.duration)
        writer.writeUnsignedShort(self.origType)
        writer.writeInt32(self.color)
        writer.writeBool(self.armorPierce)
        
