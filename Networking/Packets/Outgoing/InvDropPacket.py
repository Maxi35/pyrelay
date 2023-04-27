from Data.SlotObjectData import *

class InvDropPacket:
    def __init__(self):
        self.type = "INVDROP"
        self.slotObject = SlotObjectData()
        self.unknownShort = -1

    def write(self, writer):
        self.slotObject.write(writer)

    def read(self, reader):
        self.slotObject.read(reader)
        self.unknownShort = reader.readShort()
