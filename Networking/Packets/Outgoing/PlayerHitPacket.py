from Data.WorldPosData import *

class PlayerHitPacket:
    def __init__(self):
        self.type = "PLAYERHIT"
        self.bulletId = 0
        self.objectId = 0

    def write(self, writer):
        writer.writeByte(self.bulletId)
        writer.writeInt32(self.objectId)

    def read(self, reader):
        self.bulletId = reader.readByte()
        self.objectId = reader.readInt32()
