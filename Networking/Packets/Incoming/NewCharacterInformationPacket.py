from Networking.Packets.Packet import Packet

class NewCharacterInformationPacket(Packet):
    def __init__(self):
        self.type = "NEWCHARACTERINFORMATION"
        self.charXML = ""

    def read(self, reader):
        self.charXML = reader.readStr()

    def write(self, writer):
        writer.writeStr(self.charXML)
