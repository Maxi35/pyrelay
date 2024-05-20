from Networking.Packets.Packet import Packet

class CheckCreditsPacket(Packet):
    def __init__(self):
        self.type = "CHECKCREDITS"

    def write(self, writer):
        pass

    def read(self, reader):
        pass
