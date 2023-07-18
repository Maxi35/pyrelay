class TextPacket:
    def __init__(self):
        self.type = "TEXT"
        self.send = True
        self.name = ""
        self.objectId = 0
        self.numStars = 0
        self.bubbleTime = 0
        self.recipient = ""
        self.text = ""
        self.cleanText = ""
        self.isSupporter = False
        self.starBg = 0

    def read(self, reader):
        self.name = reader.readStr()
        self.objectId = reader.readInt32()
        self.numStars = reader.readUnsignedShort()
        self.bubbleTime = reader.readUnsignedByte()
        self.recipient = reader.readStr()
        self.text = reader.readStr()
        self.cleanText = reader.readStr()
        self.isSupporter = reader.readBool()
        self.starBg = reader.readInt32()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeInt32(self.objectId)
        writer.writeUnsignedShort(self.numStars)
        writer.writeUnsignedByte(self.bubbleTime)
        writer.writeStr(self.recipient)
        writer.writeStr(self.text)
        writer.writeStr(self.cleanText)
        writer.writeBool(self.isSupporter)
        writer.writeInt32(self.starBg)
