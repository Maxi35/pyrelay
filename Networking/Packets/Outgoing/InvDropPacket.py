from Data.SlotObjectData import *

class InvDropPacket:
    def __init__(self):
        self.type = "INVDROP"
        self.send = True
        self.slotObject = SlotObjectData()
        self.unknownByte = -1

    def write(self, writer):
        self.slotObject.write(writer)
        writer.writeByte(self.unknownByte)

    def read(self, reader):
        self.slotObject.read(reader)
        self.unknownByte = reader.readByte()
