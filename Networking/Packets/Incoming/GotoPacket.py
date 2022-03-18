from Data.WorldPosData import *

class GotoPacket:
    def __init__(self):
        self.type = "GOTO"
        self.objectId = 0
        self.position = WorldPosData()

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.position.read(reader)
