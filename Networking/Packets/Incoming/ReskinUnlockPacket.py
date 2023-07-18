class ReskinUnlockPacket:
    def __init__(self):
        self.type = "RESKINUNLOCK"
        self.send = True
        self.skinID = 0
        self.isPetSkin = 0

    def read(self, reader):
        self.skinID = reader.readInt32()
        self.isPetSkin = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.skinID)
        writer.writeInt32(self.isPetSkin)
