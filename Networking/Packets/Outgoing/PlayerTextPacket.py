class PlayerTextPacket:
    def __init__(self):
        self.type = "PLAYERTEXT"
        self.text = ""

    def write(self, writer):
        writer.writeStr(self.text)

    def read(self, reader):
        self.text = reader.readStr()
