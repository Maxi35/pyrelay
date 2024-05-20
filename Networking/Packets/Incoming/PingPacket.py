from Networking.Packets.Packet import Packet

class PingPacket(Packet):
    def __init__(self):
        self.type = "PING"
        self.serial = 0

    def read(self, reader):
        self.serial = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.serial)
