from Networking.Packets.Packet import Packet

class RealmScorePacket(Packet):
    def __init__(self):
        self.type = "REALMSCORE"
        self.score = 0

    def read(self, reader):
        self.score = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.score)
