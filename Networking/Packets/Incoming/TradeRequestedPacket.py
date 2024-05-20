from Networking.Packets.Packet import Packet

class TradeRequestedPacket(Packet):
    def __init__(self):
        self.type = "TRADEREQUESTED"
        self.name = ""

    def read(self, reader):
        self.name = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.name)
