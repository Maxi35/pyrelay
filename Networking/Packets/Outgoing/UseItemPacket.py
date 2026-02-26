from Networking.Packets.Packet import Packet
from Data.SlotObjectData import *
from Data.WorldPosData import *

class UseItemPacket(Packet):
    def __init__(self):
        self.type = "USEITEM"
        self.time = 0
        self.slotObject = SlotObjectData()
        self.pos = WorldPosData()
        self.useType = 0
        self.unknownInt = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        self.slotObject.write(writer)
        self.pos.write(writer)
        writer.writeByte(self.useType)
        writer.writeInt32(self.unknownInt)

    def read(self, reader):
        self.time = reader.readInt32()
        self.slotObject.read(reader)
        self.pos.read(reader)
        self.useType = reader.readByte()
        self.unknownInt = reader.readInt32()
