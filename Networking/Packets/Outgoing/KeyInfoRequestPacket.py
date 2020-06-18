class KeyInfoRequestPacket:
    def __init__(self):
        self.type = "KEYINFOREQUEST"
        self.itemType = 0

    def write(self, writer):
        writer.writeInt32(self.itemType)
