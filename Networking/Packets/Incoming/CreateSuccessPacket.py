class CreateSuccessPacket:
    def __init__(self):
        self.type = "CREATESUCCESS"
        self.objectId = 0
        self.charId = 0
        self.unknownStr = ""

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.charId = reader.readInt32()
        self.unknownStr = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.objectId)
        writer.writeInt32(self.charId)
        writer.writeStr(self.unknownStr)
