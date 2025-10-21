from Networking.Packets.Packet import Packet

class CrucibleResponsePacket(Packet):
    def __init__(self):
        self.type = "CRUCIBLERESPONSE"
        self.int1 = 0
        self.int2 = 0
        self.int3 = 0
        self.int4 = 0
        
        self.json1 = ""
        self.json2 = ""
        self.json3 = ""

    def write(self, writer):
        writer.writeInt32(self.int1)
        writer.writeInt32(self.int2)
        writer.writeInt32(self.int3)
        writer.writeInt32(self.int4)
        
        writer.writeStr(self.json1)
        writer.writeStr(self.json2)
        writer.writeStr(self.json3)

    def read(self, reader):
        self.int1 = reader.readInt32()
        self.int2 = reader.readInt32()
        self.int3 = reader.readInt32()
        self.int4 = reader.readInt32()
        
        self.json1 = reader.readStr()
        self.json2 = reader.readStr()
        self.json3 = reader.readStr()
