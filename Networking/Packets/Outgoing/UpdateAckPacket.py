from Networking.Packets.Packet import Packet

class UpdateAckPacket(Packet):
    def __init__(self):
        self.type = "UPDATEACK"

    def write(self, writer):
        return

    def read(self, reader):
        return
