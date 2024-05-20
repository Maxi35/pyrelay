from Networking.Packets.Packet import Packet

class ClaimDailyLoginRewardPacket(Packet):
    def __init__(self):
        self.type = "CLAIMDAILYLOGINREWARD"
        self.claimStr = ""
        self.claimType = ""

    def write(self, writer):
        writer.writeStr(self.claimStr)
        writer.writeStr(self.claimType)

    def read(self, reader):
        self.claimStr = reader.readStr()
        self.claimType = reader.readStr()
