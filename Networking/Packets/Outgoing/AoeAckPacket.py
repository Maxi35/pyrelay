from Data.WorldPosData import *

class AoeAckPacket:
    def __init__(self):
        self.type = "AOEACK"
        self.send = True
        self.time = 0
        self.pos = WorldPosData()

    def write(self, writer):
        writer.writeInt32(self.time)
        self.pos.write(writer)

    def read(self, reader):
        self.time = reader.readInt32()
        self.pos.read(reader)
