class KeyInfoRequestPacket:
    def __init__(self):
        self.type = "KEYINFOREQUEST"
        self.send = True
        self.itemType = 0

    def write(self, writer):
        writer.writeInt32(self.itemType)

    def read(self, reader):
        self.itemType = reader.readInt32()
