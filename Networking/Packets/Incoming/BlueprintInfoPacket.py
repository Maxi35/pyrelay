from Networking.Packets.Packet import Packet

class BlueprintInfoPacket(Packet):
    def __init__(self):
        self.type = "BLUEPRINTINFO"
        self.unknownByte = -1
        self.blueprints = []

    def read(self, reader):
        self.unknownByte = reader.readByte()
        numBlueprints = reader.readCompressedInt()
        for i in range(numBlueprints):
            self.blueprints.append(reader.readCompressedInt())
            
    def write(self, writer):
        writer.writeByte(self.unknownByte)
        writer.writeCompressedInt(len(self.blueprints))
        for i in range(len(self.blueprints)):
            writer.writeCompressedInt(self.blueprints[i])
