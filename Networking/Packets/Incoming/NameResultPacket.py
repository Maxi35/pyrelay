from Networking.Packets.Packet import Packet

class NameResultPacket(Packet):
    def __init__(self):
        self.type = "NAMERESULT"
        self.success = False
        self.errorText = ""

    def read(self, reader):
        self.success = reader.readBool()
        self.errorText = reader.readStr()

    def write(self, writer):
        writer.writeBool(self.success)
        writer.writeStr(self.errorText)
