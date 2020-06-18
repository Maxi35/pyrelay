class CreateGuildPacket:
    def __init__(self):
        self.type = "CREATEGUILD"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)
