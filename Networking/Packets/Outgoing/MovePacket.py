from Data.WorldPosData import *
from Data.MoveRecord import *

class MovePacket:
    def __init__(self):
        self.type = "MOVE"
        self.tickId = 0
        self.time = 0
        self.newPos = WorldPosData()
        self.records = []

    def write(self, writer):
        writer.writeInt32(self.tickId)
        writer.writeInt32(self.time)
        self.newPos.write(writer)
        writer.writeShort(len(self.records))
        for record in self.records:
            record.write(writer)
