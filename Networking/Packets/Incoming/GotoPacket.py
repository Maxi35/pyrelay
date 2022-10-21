from Data.WorldPosData import *

class GotoPacket:
    def __init__(self):
        self.type = "GOTO"
        self.objectId = 0
        self.position = WorldPosData()
        self.unknownInt = 0

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.position.read(reader)
        self.unknownInt = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.objectId)
        self.position.write(writer)
        writer.writeInt32(self.unknownInt)
