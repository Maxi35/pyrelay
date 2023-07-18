from Data.WorldPosData import *

class PlayerHitPacket:
    def __init__(self):
        self.type = "PLAYERHIT"
        self.send = True
        self.bulletId = 0
        self.objectId = 0

    def write(self, writer):
        writer.writeShort(self.bulletId)
        writer.writeInt32(self.objectId)

    def read(self, reader):
        self.bulletId = reader.readShort()
        self.objectId = reader.readInt32()
