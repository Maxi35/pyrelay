from Networking.Packets.Packet import Packet

class ResetDailyQuestsPacket(Packet):
    def __init__(self):
        self.type = "RESETDAILYQUESTS"

    def write(self, writer):
        pass

    def read(self, reader):
        pass
