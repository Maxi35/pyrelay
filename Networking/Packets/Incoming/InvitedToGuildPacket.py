from Networking.Packets.Packet import Packet

class InvitedToGuildPacket(Packet):
    def __init__(self):
        self.type = "INVITEDTOGUILD"
        self.name = ""
        self.guildName = ""

    def read(self, reader):
        self.name = reader.readStr()
        self.guildName = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeStr(self.guildName)
