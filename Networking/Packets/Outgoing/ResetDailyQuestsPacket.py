class ResetDailyQuestsPacket:
    def __init__(self):
        self.type = "RESETDAILYQUESTS"
        self.send = True

    def write(self, writer):
        pass

    def read(self, reader):
        pass
