from Data.SlotObjectData import SlotObjectData

class ForgeResponsePacket:
    def __init__(self):
        self.type = "FORGERESPONSE"
        self.slot = SlotObjectData()

    def read(self, reader):
        thing = reader.readShort()
        if thing > 0:
            self.slot.read(reader)

    def write(self, writer):
        self.slot.write(writer)
