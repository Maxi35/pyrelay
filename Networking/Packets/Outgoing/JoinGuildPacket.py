from Networking.Packets.Packet import Packet

class JoinGuildPacket(Packet):
    def __init__(self):
        self.type = "JOINGUILD"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
