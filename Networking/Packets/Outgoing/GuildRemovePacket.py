from Networking.Packets.Packet import Packet

class GuildRemovePacket(Packet):
    def __init__(self):
        self.type = "GUILDREMOVE"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
