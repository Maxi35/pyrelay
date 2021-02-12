from Data.SlotObjectData import SlotObjectData

class ForgeRespnsePacket:
    def __init__(self):
        self.type = "FORGERESPONSE"
        self.success = False
        self.slots = []

    def read(self, reader):
        self.success = reader.readBool()
        if self.success:
            slotLen = reader.readByte()
            for i in range(slotLen):
                slot = SlotObjectData()
                slot.read(reader)
                self.slots.append(slot)

    def write(self, writer):
        if len(slots) > 0:
            writer.writeBool(True)
        else:
            writer.writeBool(False)
        writer.writeByte(len(self.slots))
        for slot in self.slots:
            slot.write(writer)
