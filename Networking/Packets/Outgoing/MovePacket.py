from Data.WorldPosData import *
from Data.MoveRecord import *

class MovePacket:
    def __init__(self):
        self.type = "MOVE"
        self.tickId = 0
        self.time = 0
        self.records = []

    def write(self, writer):
        writer.writeInt32(self.tickId)
        writer.writeUInt32(self.time)
        writer.writeShort(len(self.records))
        for record in self.records:
            record.write(writer)

    def read(self, reader):
        self.tickId = reader.readInt32()
        self.time = reader.readInt32()
        recordLen = reader.readShort()
        for i in range(recordLen):
            record = MoveRecord()
            record.read(reader)
            self.records.append(record)
