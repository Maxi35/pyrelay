from Data.WorldPosData import *
from Data.MoveRecord import *

class MovePacket:
    def __init__(self):
        self.type = "MOVE"
        self.tickId = 0
        self.time = 0
        self.serverRealTimeMS = 0
        self.newPos = WorldPosData()
        self.records = []

    def write(self, writer):
        writer.writeInt32(self.tickId)
        writer.writeInt32(self.time)
        writer.writeUInt32(self.serverRealTimeMS)
        self.newPos.write(writer)
        writer.writeShort(len(self.records))
        for record in self.records:
            record.write(writer)

    def read(self, reader):
        self.tickId = reader.readInt32()
        self.time = reader.readInt32()
        self.serverRealTimeMS = reader.readUInt32()
        self.newPos.read(reader)
        recordLen = reader.readShort()
        for i in range(recordLen):
            record = MoveRecord()
            record.read(reader)
            self.records.append(record)
