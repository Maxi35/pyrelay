class PongPacket:
    def __init__(self):
        self.type = "PONG"
        self.send = True
        self.serial = 0
        self.time = 0

    def write(self, writer):
        writer.writeInt32(self.serial)
        writer.writeInt32(self.time)

    def read(self, reader):
        self.serial = reader.readInt32()
        self.time = reader.readInt32()
