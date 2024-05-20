from Networking.Packets.Packet import Packet

class CreatePacket(Packet):
    def __init__(self):
        self.type = "CREATE"
        self.classType = 0
        self.skinType = 0
        self.isChallenger = False
        self.isSeasonal = False

    def write(self, writer):
        writer.writeShort(self.classType)
        writer.writeShort(self.skinType)
        writer.writeBool(self.isChallenger)
        writer.writeBool(self.isSeasonal)

    def read(self, reader):
        self.classType = reader.readShort()
        self.skinType = reader.readShort()
        self.isChallenger = reader.readBool()
        self.isSeasonal = reader.readBool()
