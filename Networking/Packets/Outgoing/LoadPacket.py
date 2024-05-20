from Networking.Packets.Packet import Packet

class LoadPacket(Packet):
    def __init__(self):
        self.type = "LOAD"
        self.charId = 0
        self.isFromArena = False

    def write(self, writer):
        writer.writeInt32(self.charId)
        writer.writeBool(self.isFromArena)

    def read(self, reader):
        self.charId = reader.readInt32()
        self.isFromArena = reader.readBool()
