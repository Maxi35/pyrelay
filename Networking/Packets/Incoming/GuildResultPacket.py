class GuildResultPacket:
    def __init__(self):
        self.type = "GUILDRESULT"
        self.success = False
        self.lineBuilderJSON = ""

    def read(self, reader):
        self.success = reader.readBool()
        self.lineBuilderJSON = reader.readStr()
