class PlaySoundPacket:
    def __init__(self):
        self.type = "PLAYSOUND"
        self.ownerId = 0
        self.soundId = 0 

    def read(self, reader):
        self.ownerId = reader.readInt32()
        self.soundId = reader.readUnsignedByte()
