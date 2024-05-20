from Networking.Packets.Packet import Packet

class ChangePetSkinPacket(Packet):
    def __init__(self):
        self.type = "CHANGEPETSKIN"
        self.petId = 0
        self.skinType = 0
        self.currency = 0

    def write(self, writer):
        writer.writeInt32(self.petId)
        writer.writeInt32(self.skinType)
        writer.writeInt32(self.currency)

    def read(self, reader):
        self.petId = reader.readInt32()
        self.skinType = reader.readInt32()
        self.currency = reader.readInt32()
