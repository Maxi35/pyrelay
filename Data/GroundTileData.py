
class GroundTileData:
    def __init__(self, x=0, y=0, type=0):
        self.x = x
        self.y = y
        self.type = type

    def read(self, reader):
        self.x = reader.readShort()
        self.y = reader.readShort()
        self.type = reader.readUnsignedShort()

    def write(self, writer):
        writer.writeShort(self.x)
        writer.writeShort(self.y)
        writer.writeUnsignedShort(self.type)

    def clone(self):
        return GroundTileData(self.x, self.y, self.type)
