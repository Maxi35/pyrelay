class PongPacket:
    def __init__(self):
        self.type = "PONG"
        self.serial = 0
        self.time = 0

    def write(self, writer):
        writer.writeInt32(self.serial)
        writer.writeInt32(self.time)