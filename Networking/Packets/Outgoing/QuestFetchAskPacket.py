class QuestFetchAskPacket:
    def __init__(self):
        self.type = "QUESTFETCHASK"
        self.send = True

    def write(self, writer):
        pass

    def read(self, reader):
        pass
