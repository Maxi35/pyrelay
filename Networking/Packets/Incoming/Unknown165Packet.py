class Unknown165Packet:
    def __init__(self):
        self.type = "UNKNOWN165"
        self.send = True
        self.unknownStr = ""

    def read(self, reader):
        self.unknownStr = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.unknownStr)
