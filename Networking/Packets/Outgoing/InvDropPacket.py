from Networking.Packets.Packet import Packet
from Data.SlotObjectData import *

class InvDropPacket(Packet):
    def __init__(self):
        self.type = "INVDROP"
        self.slotObject = SlotObjectData()
        self.unknownByte = -1

    def write(self, writer):
        self.slotObject.write(writer)
        writer.writeByte(self.unknownByte)

    def read(self, reader):
        self.slotObject.read(reader)
        self.unknownByte = reader.readByte()
