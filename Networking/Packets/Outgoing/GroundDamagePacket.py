from Networking.Packets.Packet import Packet
from Data.WorldPosData import *

class GroundDamagePacket(Packet):
    def __init__(self):
        self.type = "GROUNDDAMAGE"
        self.time = 0
        self.pos = WorldPosData()

    def write(self, writer):
        writer.writeInt32(self.time)
        self.pos.write(writer)

    def read(self, reader):
        self.time = reader.readInt32()
        self.pos.read(reader)
