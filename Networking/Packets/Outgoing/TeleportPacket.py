from Networking.Packets.Packet import Packet

class TeleportPacket(Packet):
    def __init__(self):
        self.type = "TELEPORT"
        self.objectId = 0
        self.playerName = ""

    def write(self, writer):
        writer.writeInt32(self.objectId)
        writer.writeStr(self.playerName)

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.playerName = reader.readStr()
