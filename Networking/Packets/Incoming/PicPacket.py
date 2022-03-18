class PicPacket:
    def __init__(self):
        self.type = "PIC"
        self.width = 0
        self.height = 0
        self.bitmapData = []

    def read(self, reader):
        self.width = reader.readInt32()
        self.height = reader.readInt32()
        self.bitmapData = reader.readBytes(self.width * self.height * 4)
