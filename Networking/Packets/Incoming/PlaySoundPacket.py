from Networking.Packets.Packet import Packet

class PlaySoundPacket(Packet):
    def __init__(self):
        self.type = "PLAYSOUND"
        self.ownerId = 0
        self.soundId = 0 

    def read(self, reader):
        self.ownerId = reader.readInt32()
        self.soundId = reader.readUnsignedByte()

    def write(self, writer):
        writer.writeInt32(self.ownerId)
        writer.writeUnsignedByte(self.soundId)
