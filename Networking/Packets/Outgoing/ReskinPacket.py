class ReskinPacket:
    def __init__(self):
        self.type = "RESKIN"
        self.skinID = 0

    def write(self, writer):
        writer.writeInt32(self.skinID)

    def read(self, reader):
        self.skinID = reader.readInt32()
