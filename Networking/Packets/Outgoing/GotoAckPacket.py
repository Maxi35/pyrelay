class GotoAckPacket:
    def __init__(self):
        self.type = "GOTOACK"
        self.time = 0

    def write(self, writer):
        writer.writeInt32(self.time)
