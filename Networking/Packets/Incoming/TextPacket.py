class TextPacket:
    def __init__(self):
        self.type = "TEXT"
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
        self.numStars = reader.readInt32()
        self.bubbleTime = reader.readUnsignedByte()
        self.recipient = reader.readStr()
        self.text = reader.readStr()
        self.cleanText = reader.readStr()
        self.isSupporter = reader.readBool()
        self.starBg = reader.readInt32()
