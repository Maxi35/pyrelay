from Networking.Packets.Packet import Packet

class TradeDonePacket(Packet):
    def __init__(self):
        self.type = "TRADEDONE"
        self.code = 0
        self.description = ""

    def read(self, reader):
        self.code = reader.readInt32()
        self.description = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.code)
        writer.writeStr(self.description)
