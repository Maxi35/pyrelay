class EscapePacket:
    def __init__(self):
        self.type = "ESCAPE"
        self.send = True

    def write(self, writer):
        pass

    def read(self, reader):
        pass
