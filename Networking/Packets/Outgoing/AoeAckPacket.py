from Data.WorldPosData import *

class AoeAckPacket:
    def __init__(self):
        self.type = "AOEACK"
        self.time = 0
        self.pos = WorldPosData()

    def write(self, writer):
        writer.writeInt32(self.time)
        self.pos.writeTo(writer)
