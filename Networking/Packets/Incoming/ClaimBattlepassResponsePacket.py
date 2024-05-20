from Networking.Packets.Packet import Packet

class ClaimBattlepassResponsePacket(Packet):
    def __init__(self):
        self.type = "CLAIMBATTLEPASSRESPONSE"
        self.success = False

    def write(self, writer):
        writer.writeBool(self.success)

    def read(self, reader):
        self.success = reader.readBool()
