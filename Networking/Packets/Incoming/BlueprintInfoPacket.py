class BlueprintInfoPacket:
    def __init__(self):
        self.type = "BLUEPRINTINFO"
        self.blueprints = []

    def read(self, reader):
        numBlueprints = reader.readByte()
        for i in range(numBlueprints):
            self.blueprints.append(reader.readCompressedInt())
            
    def write(self, writer):
        writer.writeByte(len(self.blueprints))
        for i in range(len(self.blueprints)):
            writer.writeCompressedInt(self.blueprints[i])
