class PingPacket:
    def __init__(self):
        self.type = "PING"
        self.serial = 0

    def read(self, reader):
        self.serial = reader.readInt32()
