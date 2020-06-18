
class MoveRecord:
    def __init__(self, time=0, x=0, y=0):
        self.time = time
        self.x = x
        self.y = y

    def read(self, reader):
        self.time = reader.readInt32()
        self.x = reader.readFloat()
        self.y = reader.readFloat()

    def write(self, writer):
        writer.writeInt32(time)
        writer.writeFloat(y)
        writer.writeFloat(y)

    def clone(self):
        return MoveRecord(self.time, self.x, self.y)
