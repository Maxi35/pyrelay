from Networking.Packets.Packet import Packet

class VerifyEmailPacket(Packet):
    def __init__(self):
        self.type = "VERIFYEMAIL"

    def read(self, reader):
        pass

    def write(self, writer):
        pass
