class SendEmotePacket:
    def __init__(self):
        self.type = "SENDEMOTE"
        self.send = True
        self.emoteId = -1
        self.time = -1
        self.unknownByte = -1

    def write(self, writer):
        writer.writeInt32(self.emoteId)
        writer.writeInt32(self.time)
        writer.writeByte(self.unknownByte)

    def read(self, reader):
        self.emoteId = reader.readInt32()
        self.time = reader.readInt32()
        self.unknownByte = reader.readByte()
