class LoadPacket:
    def __init__(self):
        self.type = "LOAD"
        self.charId = 0
        self.isFromArena = False
        self.isChallenger = False

    def write(self, writer):
        writer.writeInt32(self.charId)
        writer.writeBool(self.isFromArena)
        writer.writeBool(self.isChallenger)
