from Data.WorldPosData import *

class ShowEffectPacket:
    def __init__(self):
        self.type = "SHOWEFFECT"
        self.effectType = 0
        self.ignore = 0
        self.targetObjectId = 0
        self.pos1 = WorldPosData()
        self.pos2 = WorldPosData()
        self.color = 0
        self.duration = 0
        self.extra = False
        self.unknownByte = 0

    def read(self, reader):
        self.effectType = reader.readUnsignedByte()
        self.ignore = reader.readUnsignedByte()#Better way to do this?
            
        if self.ignore&64:
            self.targetObjectId = reader.readCompressedInt()
        else:
            self.targetObjectId = 0
            
        if self.ignore&2:
            self.pos1.x = reader.readFloat()
        else:
            self.pos1.x = 0
            
        if self.ignore&4:
            self.pos1.y = reader.readFloat()
        else:
            self.pos1.y = 0
            
        if self.ignore&8:
            self.pos2.x = reader.readFloat()
        else:
            self.pos2.x = 0
            
        if self.ignore&16:
            self.pos2.y = reader.readFloat()
        else:
            self.pos2.y = 0
            
        if self.ignore&1:
            self.color = reader.readInt32()
        else:
            self.color = 0
            
        if self.ignore&32:
            self.duration = reader.readFloat()
        else:
            self.duration = 0

        if reader.bytesAvailable():
            self.extra = True
            self.unknownByte = reader.readByte()

    def write(self, writer):
        writer.writeUnsignedByte(self.effectType)
        writer.writeUnsignedByte(self.ignore)

        if self.ignore&64:
            writer.writeCompressedInt(self.targetObjectId)
            
        if self.ignore&2:
            writer.writeFloat(self.pos1.x)
            
        if self.ignore&4:
            writer.writeFloat(self.pos1.y)
            
        if self.ignore&8:
            writer.writeFloat(self.pos2.x)
            
        if self.ignore&16:
            writer.writeFloat(self.pos2.y)
            
        if self.ignore&1:
            writer.writeInt32(self.color)
            
        if self.ignore&32:
            writer.writeFloat(self.duration)

        if self.extra:
            writer.writeByte(self.unknownByte)
