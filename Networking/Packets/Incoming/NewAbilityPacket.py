class NewAbilityPacket:
    def __init__(self):
        self.type = "NEWABILITY"
        self.abilityType = 0

    def read(self, reader):
        self.abilityType = reader.readInt32()
