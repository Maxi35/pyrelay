class CreateSuccessPacket:
    def __init__(self):
        self.type = "CREATESUCCESS"
        self.objectId = 0
        self.charId = 0

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.charId = reader.readInt32()
