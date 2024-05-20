from Networking.Packets.Packet import Packet

class SendEmotePacket(Packet):
    def __init__(self):
        self.type = "SENDEMOTE"
        self.emoteId = -1
        self.time = -1
        self.unknownByte = -1

    def write(self, writer):
        writer.writeInt32(self.emoteId)
        writer.writeInt32(self.time)
        writer.writeByte(self.unknownByte)

    def read(self, reader):
        self.emoteId = reader.readInt32()
        self.time = reader.readInt32()
        self.unknownByte = reader.readByte()
