class NotificationPacket:
    def __init__(self):
        self.type = "NOTIFICATION"
        self.unknown1 = 0
        self.unknown2 = 0
        self.message = ""
        self.unknowns = []

    def read(self, reader):
        self.unknown1 = reader.readByte()
        self.unknown2 = reader.readByte()
        self.message = reader.readStr()
        while reader.bytesAvailable() > 0:
            self.unknowns.append(reader.readByte())

    def write(self, writer):
        writer.writeByte(self.unknown1)
        writer.writeByte(self.unknown2)
        writer.writeStr(self.message)
        for byte in self.unknowns:
            writer.writeByte(byte)
