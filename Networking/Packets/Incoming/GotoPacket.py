from Networking.Packets.Packet import Packet
from Data.WorldPosData import *

class GotoPacket(Packet):
    def __init__(self):
        self.type = "GOTO"
        self.objectId = 0
        self.pos = WorldPosData()
        self.unknownInt = 0

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.pos.read(reader)
        self.unknownInt = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.objectId)
        self.pos.write(writer)
        writer.writeInt32(self.unknownInt)
