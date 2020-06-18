class NotificationPacket:
    def __init__(self):
        self.type = "NOTIFICATION"
        self.objectId = 0
        self.message = ""
        self.color = 0

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.message = reader.readStr()
        self.color = reader.readInt32()
