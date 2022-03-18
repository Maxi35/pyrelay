class InvitedToGuildPacket:
    def __init__(self):
        self.type = "INVITEDTOGUILD"
        self.name = ""
        self.guildName = ""

    def read(self, reader):
        self.name = reader.readStr()
        self.guildName = reader.readStr()
