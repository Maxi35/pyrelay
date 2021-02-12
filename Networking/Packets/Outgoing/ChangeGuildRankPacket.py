class ChangeGuildRankPacket:
    def __init__(self):
        self.type = "CHANGEGUILDRANK"
        self.name = ""
        self.guildRank = 0

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeByte(self.guildRank)

    def read(self, reader):
        self.name = reader.readStr()
        self.guildRank = reader.readByte()
