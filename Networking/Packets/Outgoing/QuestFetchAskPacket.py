from Networking.Packets.Packet import Packet

class QuestFetchAskPacket(Packet):
    def __init__(self):
        self.type = "QUESTFETCHASK"

    def write(self, writer):
        pass

    def read(self, reader):
        pass
