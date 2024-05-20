from Networking.Packets.Packet import Packet

class BuyResultPacket(Packet):
    def __init__(self):
        self.type = "BUYRESULT"
        self.result = 0
        self.resultString = ""

    def read(self, reader):
        self.result = reader.readInt32()
        self.resultString = reader.readStr()
        
    def write(self, writer):
        writer.writeInt32(self.result)
        writer.writeStr(self.resultString)
