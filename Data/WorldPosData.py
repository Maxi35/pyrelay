
class WorldPosData:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distTo(self, a, b=None):
        if isinstance(a, self):
            return ((self.x-a.x)**2 + (self.y-a.y)**2)**0.5
        elif not b is None:
            return ((self.x-a)**2 + (self.y-b)**2)**0.5
        raise ValueError("Wrong arguments for 'distTo'")

    def read(self, reader):
        self.x = reader.readFloat()
        self.y = reader.readFloat()

    def write(self, writer):
        writer.writeFloat(self.x)
        writer.writeFloat(self.y)

    def clone(self):
        return WorldPosData(self.x, self.y)

    def squareDist(self, other):
        return (self.x-other.x)**2 + (self.y-other.y)**2

    def dist(self, other):
        return self.squareDist(other)**0.5

    def __str__(self):
        return "{}, {}".format(round(self.x, 2), round(self.y, 2))

    def __add__(self, other):
        pos = self.clone()
        if type(other) == WorldPosData:
            pos.x += other.x
            pos.y += other.y
        elif type(other) in [list, tuple]:#Should prob do some checks
            pos.x += other[0]
            pos.y += other[1]
        elif type(other) == dict:
            pos.x += other["x"]
            pos.y += other["y"]
        return pos
