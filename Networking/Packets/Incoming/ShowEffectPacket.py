from Data.WorldPosData import *

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
        self.effectType = reader.readInt32()
        self.pos1.read(reader)
        self.pos2.read(reader)
        self.color = reader.readInt32()
        self.duration = reader.readFloat()
