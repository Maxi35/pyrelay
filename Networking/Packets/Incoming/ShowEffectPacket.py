from Data.WorldPosData import *
import Data.CompressedInt as CompressedInt

class ShowEffectPacket:
    def __init__(self):
        self.type = "SHOWEFFECT"
        self.effectType = 0
        self.targetObjectId = 0
        self.pos1 = WorldPosData()
        self.pos2 = WorldPosData()
        self.color = 0
        self.duration = 0

    def read(self, reader):
        self.effectType = reader.readUnsignedByte()
        ignore = reader.readUnsignedByte()#Better way to do this?
        if ignore&64:
            self.targetObjectId = CompressedInt.read(reader)
        else:
            self.targetObjectId = 0
            
        if ignore&2:
            self.pos1.x = reader.readFloat()
        else:
            self.pos1.x = 0
            
        if ignore&4:
            self.pos1.y = reader.readFloat()
        else:
            self.pos1.y = 0
            
        if ignore&8:
            self.pos2.x = reader.readFloat()
        else:
            self.pos2.x = 0
            
        if ignore&16:
            self.pos2.x = reader.readFloat()
        else:
            self.pos2.x = 0
            
        if ignore&1:
            self.color = reader.readInt32()
        else:
            self.color = 0
            
        if ignore&32:
            self.duration = reader.readFloat()
        else:
            self.duration = 0
