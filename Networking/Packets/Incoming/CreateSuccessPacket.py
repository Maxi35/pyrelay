from Networking.Packets.Packet import Packet

class CreateSuccessPacket(Packet):
    def __init__(self):
        self.type = "CREATESUCCESS"
        self.objectId = 0
        self.charId = 0
        self.PCStats = ""

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.charId = reader.readInt32()
        self.PCStats = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.objectId)
        writer.writeInt32(self.charId)
        writer.writeStr(self.PCStats)
