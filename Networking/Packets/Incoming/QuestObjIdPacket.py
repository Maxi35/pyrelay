class QuestObjIdPacket:
    def __init__(self):
        self.type = "QUESTOBJID"
        self.send = True
        self.objectId = 0
        self.unknownBytes = []

    def read(self, reader):
        self.objectId = reader.readInt32()
        for i in range(reader.bytesAvailable()):
            self.unknownBytes.append(reader.readByte())

    def write(self, writer):
        writer.writeInt32(self.objectId)
        for i in range(len(self.unknownBytes)):
            writer.writeByte(self.unknownBytes[i])
