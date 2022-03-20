from Data.GroundTileData import *
from Data.ObjectData import *
from Data.WorldPosData import *
import Data.CompressedInt as CompressedInt

class UpdatePacket:
    def __init__(self):
        self.type = "UPDATE"
        self.pos = WorldPosData()
        self.levelType = 0
        self.tiles = []
        self.newObjs = []
        self.drops = []

    def read(self, reader):
        self.pos.read(reader)
        self.levelType = reader.readByte()
        tiles_len = CompressedInt.read(reader)
        for i in range(tiles_len):
            tile = GroundTileData()
            tile.read(reader)
            self.tiles.append(tile)
        objects_len = CompressedInt.read(reader)
        for i in range(objects_len):
            data = ObjectData()
            data.read(reader)
            self.newObjs.append(data)
        drops_len = CompressedInt.read(reader)
        for i in range(drops_len):
            self.drops.append(CompressedInt.read(reader))