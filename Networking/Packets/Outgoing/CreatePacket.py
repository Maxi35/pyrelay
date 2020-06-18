class CreatePacket:
    def __init__(self):
        self.type = "CREATE"
        self.classType = 0
        self.skinType = 0
        self.isChallenger = False

    def write(self, writer):
        writer.writeShort(self.classType)
        writer.writeShort(self.skinType)
        writer.writeBool(self.isChallenger)
