from Networking.Packets.Packet import Packet

class Unknown165Packet(Packet):
    def __init__(self):
        self.type = "UNKNOWN165"
        self.unknownStr = ""

    def read(self, reader):
        self.unknownStr = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.unknownStr)
