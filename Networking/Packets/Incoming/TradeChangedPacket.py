from Networking.Packets.Packet import Packet

class TradeChangedPacket(Packet):
    def __init__(self):
        self.type = "TRADECHANGED"
        self.offer = []

    def read(self, reader):
        offer_len = reader.readShort()
        for i in range(offer_len):
            self.offer.append(reader.readBool())

    def write(self, writer):
        writer.writeShort(len(self.offer))
        for i in range(len(self.offer)):
            writer.writeBool(self.offer[i])
