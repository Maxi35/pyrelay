#Fame bonuses given on death

class FameData:
    def __init__(self, name=0, rank=0, fame=0):
        self.name = name
        self.rank = rank
        self.fame = fame

    def read(self, reader):
        self.name = reader.readStr()
        self.rank = reader.readCompressedInt()
        self.fame = reader.readCompressedInt()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeCompressedInt(self.rank)
        writer.writeCompressedInt(self.fame)

    def clone(self):
        return StatData(self.statType, self.statValue, self.strStatValue, self.secondaryValue)

    def __str__(self):
        return f"{self.name}-{self.rank} {self.fame}"
