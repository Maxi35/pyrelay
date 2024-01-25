from Data.WorldPosData import WorldPosData

class MoveRecord:
    def __init__(self, time=0, x=0.0, y=0.0):
        self.time = time
        self.pos = WorldPosData(x, y)

    def read(self, reader):
        self.time = reader.readInt32()
        self.pos.read(reader)

    def write(self, writer):
        writer.writeInt32(self.time)
        self.pos.write(writer)

    def clone(self):
        return MoveRecord(self.time, self.pos.x, self.pos.y)

    def __str__(self):
        return f"time: {self.time}, pos: {self.pos}"

    def __repr__(self):
        return str(self)