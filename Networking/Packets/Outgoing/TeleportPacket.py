class TeleportPacket:
    def __init__(self):
        self.type = "TELEPORT"
        self.objectId = 0

    def write(self, writer):
        writer.writeInt32(self.objectId)

    def read(self, reader):
        self.objectId = reader.readInt32()
