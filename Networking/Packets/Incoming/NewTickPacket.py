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
