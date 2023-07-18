class UpdateAckPacket:
    def __init__(self):
        self.type = "UPDATEACK"
        self.send = True

    def write(self, writer):
        return

    def read(self, reader):
        return
