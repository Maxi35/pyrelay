class GoToQuestRoomPacket:
    def __init__(self):
        self.type = "GOTOQUESTROOM"
        self.send = True

    def write(self, writer):
        pass

    def read(self, reader):
        pass
