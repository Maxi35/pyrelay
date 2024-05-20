from Networking.Packets.Packet import Packet

class ClaimDailyLoginResponsePacket(Packet):
    def __init__(self):
        self.type = "CLAIMDAILYLOGINRESPONSE"
        self.itemId = 0
        self.quantity = 0
        self.gold = 0

    def read(self, reader):
        self.itemId = reader.readInt32()
        self.quantity = reader.readInt32()
        self.gold = reader.readInt32()
        
    def write(self, writer):
        writer.writeInt32(self.itemId)
        writer.writeInt32(self.quantity)
        writer.writeInt32(self.gold)
