class NewAbilityPacket:
    def __init__(self):
        self.type = "NEWABILITY"
        self.abilityType = 0

    def read(self, reader):
        self.abilityType = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.abilityType)
