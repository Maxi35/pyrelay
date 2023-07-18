class PlaySoundPacket:
    def __init__(self):
        self.type = "PLAYSOUND"
        self.send = True
        self.ownerId = 0
        self.soundId = 0 

    def read(self, reader):
        self.ownerId = reader.readInt32()
        self.soundId = reader.readUnsignedByte()

    def write(self, writer):
        writer.writeInt32(self.ownerId)
        writer.writeUnsignedByte(self.soundId)
