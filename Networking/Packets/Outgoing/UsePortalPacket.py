from Networking.Packets.Packet import Packet

class UsePortalPacket(Packet):
    def __init__(self):
        self.type = "USEPORTAL"
        self.objectId = 0

    def write(self, writer):
        writer.writeInt32(self.objectId)

    def read(self, reader):
        self.objectId = reader.readInt32()
