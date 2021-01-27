class LoadPacket:
    def __init__(self):
        self.type = "LOAD"
        self.charId = 0
        self.isChallenger = False

    def write(self, writer):
        writer.writeInt32(self.charId)
        writer.writeBool(self.isChallenger)

    def read(self, reader):
        self.charId = reader.readInt32()
        self.isChallenger = reader.readBool()
