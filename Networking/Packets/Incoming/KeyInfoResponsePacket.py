from Networking.Packets.Packet import Packet

class KeyInfoResponsePacket(Packet):
    def __init__(self):
        self.type = "KEYINFORESPONSE"
        self.name = ""
        self.description = ""
        self.creator = ""

    def read(self, reader):
        self.name = reader.readStr()
        self.description = reader.readStr()
        self.creator = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeStr(self.description)
        writer.writeStr(self.creator)
