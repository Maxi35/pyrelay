class CreatePacket:
    def __init__(self):
        self.type = "CREATE"
        self.classType = 0
        self.skinType = 0

    def write(self, writer):
        writer.writeShort(self.classType)
        writer.writeShort(self.skinType)

    def read(self, reader):
        self.classType = reader.readShort()
        self.skinType = reader.readShort()
