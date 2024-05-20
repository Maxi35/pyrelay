from Networking.Packets.Packet import Packet

class GuildInvitePacket(Packet):
    def __init__(self):
        self.type = "GUILDINVITE"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
