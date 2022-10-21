class ExaltationUpdatePacket:
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
        self.dexProgress = reader.readByte()
        self.spdProgress = reader.readByte()
        self.vitProgress = reader.readByte()
        self.wisProgress = reader.readByte()
        self.defProgress = reader.readByte()
        self.attProgress = reader.readByte()
        self.manaProgress = reader.readByte()
        self.lifeProgress = reader.readByte()
        
    def write(self, writer):
        writer.writeShort(self.objType)
        writer.writeByte(self.dexProgress)
        writer.writeByte(self.spdProgress)
        writer.writeByte(self.vitProgress)
        writer.writeByte(self.wisProgress)
        writer.writeByte(self.defProgress)
        writer.writeByte(self.attProgress)
        writer.writeByte(self.manaProgress)
        writer.writeByte(self.lifeProgress)
