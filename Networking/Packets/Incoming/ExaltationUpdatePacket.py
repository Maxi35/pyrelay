from Networking.Packets.Packet import Packet

class ExaltationUpdatePacket(Packet):
    def __init__(self):
        self.type = "EXALTATIONUPDATE"
        self.objType = -1
        self.dexProgress = -1
        self.spdProgress = -1
        self.vitProgress = -1
        self.wisProgress = -1
        self.defProgress = -1
        self.attProgress = -1
        self.manaProgress = -1
        self.lifeProgress = -1

    def read(self, reader):
        self.objType = reader.readShort()
        self.dexProgress = reader.readCompressedInt()
        self.spdProgress = reader.readCompressedInt()
        self.vitProgress = reader.readCompressedInt()
        self.wisProgress = reader.readCompressedInt()
        self.defProgress = reader.readCompressedInt()
        self.attProgress = reader.readCompressedInt()
        self.manaProgress = reader.readCompressedInt()
        self.lifeProgress = reader.readCompressedInt()
        
    def write(self, writer):
        writer.writeShort(self.objType)
        writer.writeCompressedInt(self.dexProgress)
        writer.writeCompressedInt(self.spdProgress)
        writer.writeCompressedInt(self.vitProgress)
        writer.writeCompressedInt(self.wisProgress)
        writer.writeCompressedInt(self.defProgress)
        writer.writeCompressedInt(self.attProgress)
        writer.writeCompressedInt(self.manaProgress)
        writer.writeCompressedInt(self.lifeProgress)
