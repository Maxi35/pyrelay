
class QueueInformationPacket:
    def __init__(self):
        self.type = "QUEUEINFORMATION"
        self.curPos = -1
        self.maxPos = -1

    def read(self, reader):
        self.curPos = reader.readUnsignedShort()
        self.maxPos = reader.readUnsignedShort()
