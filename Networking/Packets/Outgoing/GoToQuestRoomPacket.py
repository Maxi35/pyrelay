from Networking.Packets.Packet import Packet

class GoToQuestRoomPacket(Packet):
    def __init__(self):
        self.type = "GOTOQUESTROOM"

    def write(self, writer):
        pass

    def read(self, reader):
        pass
