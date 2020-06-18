class GuildInvitePacket:
    def __init__(self):
        self.type = "GUILDINVITE"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)
