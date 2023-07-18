class InvitedToGuildPacket:
    def __init__(self):
        self.type = "INVITEDTOGUILD"
        self.send = True
        self.name = ""
        self.guildName = ""

    def read(self, reader):
        self.name = reader.readStr()
        self.guildName = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeStr(self.guildName)
