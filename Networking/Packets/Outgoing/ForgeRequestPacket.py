from Networking.Packets.Packet import Packet
from Data.SlotObjectData import SlotObjectData

class ForgeRequestPacket(Packet):
    def __init__(self):
        self.type = "FORGEREQUEST"
        self.itemId = -1
        self.offers = []

    def write(self, writer):
        writer.writeInt32(self.itemId)
        writer.writeInt32(len(self.offers))
        for offer in self.offers:
            offer.write(writer)

    def read(self, reader):
        self.itemId = reader.readInt32()
        offerLen = reader.readInt32()
        for i in range(offerLen):
            slotObject = SlotObjectData()
            slotObject.read(reader)
            self.offers.append(slotObject)
