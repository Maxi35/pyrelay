class ShootAckPacket:
    def __init__(self):
        self.type = "SHOOTACK"
        self.time = 0

    def write(self, writer):
        writer.writeInt32(self.time)

    def read(self, reader):
        self.time = reader.writeInt32()
