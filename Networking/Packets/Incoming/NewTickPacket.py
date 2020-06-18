from Data.ObjectStatusData import *

class NewTickPacket:
    def __init__(self):
        self.type = "NEWTICK"
        self.tickId = 0
        self.tickTime = 0
        self.statuses = []

    def read(self, reader):
        self.tickId = reader.readInt32()
        self.tickTime = reader.readInt32()
        statuses_num = reader.readShort()
        for i in range(statuses_num):
            status = ObjectStatusData()
            status.read(reader)
            self.statuses.append(status)
