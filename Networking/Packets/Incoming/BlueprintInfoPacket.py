import Data.CompressedInt as CompressedInt

class BlueprintInfoPacket:
    def __init__(self):
        self.type = "BLUEPRINTINFO"
        self.blueprints = []

    def read(self, reader):
        numBlueprints = reader.readByte()
        for i in range(numBlueprints):
            self.blueprints.append(CompressedInt.read(reader))
