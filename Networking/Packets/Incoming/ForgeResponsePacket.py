from Networking.Packets.Packet import Packet
from Data.SlotObjectData import SlotObjectData

class ForgeResponsePacket(Packet):
    def __init__(self):
        self.type = "FORGERESPONSE"
        self.success = False
        self.slots = []

    def read(self, reader):
        self.success = reader.readBool()
        slotLen = reader.readByte()
        for i in range(slotLen):
            slot = SlotObjectData()
            slot.read(reader)
            self.slots.append(slot)

    def write(self, writer):
        writer.writeBool(self.success)
        writer.writeByte(len(self.slots))
        for slot in self.slots:
            slot.write(writer)
