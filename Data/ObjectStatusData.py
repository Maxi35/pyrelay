from .WorldPosData import *
from .StatData import *

class ObjectStatusData:
    def __init__(self, objectId=0, pos=None, stats=None):
        self.objectId = objectId
        if pos is None:
            self.pos = WorldPosData()
        else:
            self.pos = pos.clone()
        if stats is None:
            self.stats = []
        else:
            self.stats = [stat.clone() for stat in stats]

    def read(self, reader):
        self.objectId = reader.readCompressedInt()
        self.pos.read(reader)
        stats_len = reader.readCompressedInt()
        for i in range(stats_len):
            stat = StatData()
            stat.read(reader)
            self.stats.append(stat)

    def write(self, writer):
        writer.writeCompressedInt(self.objectId)
        self.pos.write(writer)
        writer.writeCompressedInt(len(self.stats))
        for stat in self.stats:
            stat.write(writer)

    def clone(self):
        return ObjectStatusData(self.objectId, self.pos, [stat.clone() for stat in self.stats])

    def __str__(self):
        return "ObjectId: {}\nPos: {}\nStats: [\n{}\n]".format(self.objectId, self.pos, "\n\n".join(map(str, self.stats)))
