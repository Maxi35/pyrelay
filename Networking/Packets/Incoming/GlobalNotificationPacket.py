class GlobalNotificationPacket:
    def __init__(self):
        self.type = "GLOBALNOTIFICATION"
        self.notificationType = 0
        self.text = ""

    def read(self, reader):
        self.notificationType = reader.readInt32()
        self.text = reader.readStr()
