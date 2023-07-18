class GlobalNotificationPacket:
    def __init__(self):
        self.type = "GLOBALNOTIFICATION"
        self.send = True
        self.notificationType = 0
        self.text = ""

    def read(self, reader):
        self.notificationType = reader.readInt32()
        self.text = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.notificationType)
        writer.writeStr(self.text)
