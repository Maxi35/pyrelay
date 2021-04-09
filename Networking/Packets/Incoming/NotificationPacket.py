class NotificationPacket:
    def __init__(self):
        self.type = "NOTIFICATION"
        self.unknown1 = 0
        self.unknown2 = 0
        self.message = ""

    def read(self, reader):
        self.unknown1 = reader.readByte()
        self.unknown2 = reader.readByte()
        self.message = reader.readStr()
