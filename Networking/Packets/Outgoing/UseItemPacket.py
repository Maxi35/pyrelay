from Data.SlotObjectData import *
from Data.WorldPosData import *

class UseItemPacket:
    def __init__(self):
        self.type = "USEITEM"
        self.item = 0
        self.slotObject = SlotObjectData()
        self.pos = WorldPosData()
        self.useType = 0

    def write(self, writer):
        writer.write(self.time)
        self.slotObject.write(writer)
        self.pos.write(writer)
        writer.write(self.useType)
