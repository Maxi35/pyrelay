class JoinGuildPacket:
    def __init__(self):
        self.type = "JOINGUILD"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
