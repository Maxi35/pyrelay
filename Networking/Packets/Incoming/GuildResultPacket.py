class GuildResultPacket:
    def __init__(self):
        self.type = "GUILDRESULT"
        self.success = False
        self.lineBuilderJSON = ""

    def read(self, reader):
        self.success = reader.readBool()
        self.lineBuilderJSON = reader.readStr()

    def write(self, writer):
        writer.writeBool(self.success)
        writer.writeStr(self.lineBuilderJSON)
