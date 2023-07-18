class GuildInvitePacket:
    def __init__(self):
        self.type = "GUILDINVITE"
        self.send = True
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
