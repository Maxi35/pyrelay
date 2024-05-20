from Networking.Packets.Packet import Packet

class EscapePacket(Packet):
    def __init__(self):
        self.type = "ESCAPE"

    def write(self, writer):
        pass

    def read(self, reader):
        pass
