class UsePortalPacket:
    def __init__(self):
        self.type = "USEPORTAL"
        self.objectId = 0

    def write(self, writer):
        writer.writeInt32(self.objectId)
