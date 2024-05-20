from Networking.Packets.Packet import Packet

class ReconnectPacket(Packet):
    def __init__(self):
        self.type = "RECONNECT"
        self.name = ""
        self.host = ""
        self.port = 0
        self.gameId = 0
        self.keyTime = 0
        self.key = []

    def read(self, reader):
        self.name = reader.readStr()
        self.host = reader.readStr()
        self.port = reader.readShort()
        self.gameId = reader.readInt32()
        self.keyTime = reader.readInt32()
        self.key = reader.readBytes()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeStr(self.host)
        writer.writeShort(self.port)
        writer.writeInt32(self.gameId)
        writer.writeInt32(self.keyTime)
        writer.writeBytes(self.key)
