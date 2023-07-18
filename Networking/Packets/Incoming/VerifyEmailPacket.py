class VerifyEmailPacket:
    def __init__(self):
        self.type = "VERIFYEMAIL"
        self.send = True

    def read(self, reader):
        pass

    def write(self, writer):
        pass
