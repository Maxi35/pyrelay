class ReskinUnlockPacket:
    def __init__(self):
        self.type = "RESKINUNLOCK"
        self.skinID = 0
        self.isPetSkin = 0

    def read(self, reader):
        self.skinID = reader.readInt32()
        self.isPetSkin = reader.readInt32()
