from Data.ObjectStatusData import *

class NewTickPacket:
    def __init__(self):
        self.type = "NEWTICK"
        self.tickId = 0
        self.tickTime = 0
        self.serverRealTimeMS = 0
        self.serverLastTimeRTTMS = 0
        self.statuses = []

    def read(self, reader):
        self.tickId = reader.readInt32()
        self.tickTime = reader.readInt32()
        self.serverRealTimeMS = reader.readUInt32()
        self.serverLastTimeRTTMS = reader.readUnsignedShort()
        statuses_num = reader.readShort()
        for i in range(statuses_num):
            status = ObjectStatusData()
            status.read(reader)
            self.statuses.append(status)

    def write(self, writer):
        writer.writeInt32(self.tickId)
        writer.writeInt32(self.tickTime)
        writer.writeUInt32(self.serverRealTimeMS)
        writer.writeUnsignedShort(self.serverLastTimeRTTMS)
        writer.writeShort(len(self.statuses))
        for i in range(len(self.statuses)):
            self.statuses[i].write(writer)
