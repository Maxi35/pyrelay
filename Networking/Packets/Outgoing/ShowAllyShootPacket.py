class ShowAllyShootPacket:
    def __init__(self):
        self.type = "SHOWALLYSHOOT"
        self.toggle = 0

    def write(self, writer):
        writer.writeInt32(self.toggle)

    def read(self, reader):
        self.toggle = reader.writeInt32()
