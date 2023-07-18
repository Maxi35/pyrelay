class CheckCreditsPacket:
    def __init__(self):
        self.type = "CHECKCREDITS"
        self.send = True

    def write(self, writer):
        pass

    def read(self, reader):
        pass
