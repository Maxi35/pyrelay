
class MoveRecord:
    def __init__(self, time=0, x=0, y=0):
        self.time: int = time
        self.x: int = x
        self.y: int = y

    def read(self, reader) -> None:
        self.time = reader.readInt32()
        self.x = reader.readFloat()
        self.y = reader.readFloat()

    def write(self, writer) -> None:
        writer.writeInt32(self.time)
        writer.writeFloat(self.y)
        writer.writeFloat(self.y)

    def clone(self) -> object:
        return MoveRecord(self.time, self.x, self.y)
