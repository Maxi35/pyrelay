from Networking.Packets.Packet import Packet

class ReskinUnlockPacket(Packet):
    def __init__(self):
        self.type = "RESKINUNLOCK"
        self.isPetSkin = 0

    def read(self, reader):
        self.isPetSkin = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.skinID)
        writer.writeInt32(self.isPetSkin)
