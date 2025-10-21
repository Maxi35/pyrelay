from Networking.Packets.Packet import Packet
from Data.GroundTileData import *
from Data.ObjectData import *
from Data.WorldPosData import *

class UpdatePacket(Packet):
    def __init__(self):
        self.type = "UPDATE"
        self.pos = WorldPosData()
        self.levelType = 0
        self.tiles = []
        self.newObjs = []
        self.drops = []
        self.unknownByte = -1

    def read(self, reader):
        self.pos.read(reader)
        self.levelType = reader.readByte()
        tiles_len = reader.readCompressedInt()
        for i in range(tiles_len):
            tile = GroundTileData()
            tile.read(reader)
            self.tiles.append(tile)
            
        objects_len = reader.readCompressedInt()
        for i in range(objects_len):
            data = ObjectData()
            data.read(reader)
            self.newObjs.append(data)
            
        drops_len = reader.readCompressedInt()
        for i in range(drops_len):
            self.drops.append(reader.readCompressedInt())
        
        if reader.bytesAvailable() > 0:
            self.unknownByte = reader.readUnsignedByte()

    def write(self, writer):
        self.pos.write(writer)
        writer.writeByte(self.levelType)
        writer.writeCompressedInt(len(self.tiles))
        for i in range(len(self.tiles)):
            self.tiles[i].write(writer)
            
        writer.writeCompressedInt(len(self.newObjs))
        for i in range(len(self.newObjs)):
            self.newObjs[i].write(writer)
            
        writer.writeCompressedInt(len(self.drops))
        for i in range(len(self.drops)):
            writer.writeCompressedInt(self.drops[i])
        
        if self.unknownByte != -1:
            writer.writeUnsignedByte(self.unknownByte)
