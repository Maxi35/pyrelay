class ChooseNamePacket:
    def __init__(self):
        self.type = "CHOOSENAME"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
