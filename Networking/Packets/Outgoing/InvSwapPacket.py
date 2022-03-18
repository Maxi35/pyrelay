from Data.WorldPosData import *
from Data.SlotObjectData import *

class InvSwapPacket:
    def __init__(self):
        self.type = "INVSWAP"
        self.time = 0
        self.pos = WorldPosData()
        self.slotObject1 = SlotObjectData()
        self.slotObject2 = SlotObjectData()

    def write(self, writer):
        writer.writeInt32(self.time)
        self.pos.write(writer)
        self.slotObject1.write(writer)
        self.slotObject2.write(writer)

    def read(self, reader):
        self.time = reader.readInt32()
        self.pos.read(reader)
        self.slotObject1.read(reader)
        self.slotObject2.read(reader)
