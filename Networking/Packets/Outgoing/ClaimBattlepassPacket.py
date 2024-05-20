from Networking.Packets.Packet import Packet

class ClaimBattlepassPacket(Packet):
    def __init__(self):
        self.type = "CLAIMBATTLEPASS"
        self.item = -1#Index of item or -1 for all

    def write(self, writer):
        writer.writeByte(self.item)

    def read(self, reader):
        self.item = reader.readByte()
