class ChangePetSkinPacket:
    def __init__(self):
        self.type = "CHANGEPETSKIN"
        self.petId = 0
        self.skinType = 0
        self.currency = 0

    def write(self, writer):
        writer.writeInt32(self.petId)
        writer.writeInt32(self.skinType)
        writer.writeInt32(self.currency)
