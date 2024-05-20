from Networking.Packets.Packet import Packet

class CrucibleResponsePacket(Packet):
    def __init__(self):
        self.type = "CRUCIBLERESPONSE"

    def write(self, writer):
        writer.writeInt32(self.int1)
        writer.writeInt32(self.int2)
        writer.writeInt32(self.int3)
        
        writer.writeStr(self.json1)
        writer.writeStr(self.json2)

    def read(self, reader):
        self.int1 = reader.readInt32()
        self.int2 = reader.readInt32()
        self.int3 = reader.readInt32()
        
        self.json1 = reader.readStr()
        self.json2 = reader.readStr()
