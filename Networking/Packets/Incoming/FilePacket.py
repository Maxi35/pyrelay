class FilePacket:
    def __init__(self):
        self.type = "FILE"
        self.fileName = ""
        self.file = ""

    def read(self, reader):
        self.fileName = reader.readStr()
        self.file = reader.readStr32()

    def write(self, writer):
        writer.writeStr(self.fileName)
        writer.writeStr32(self.file)
