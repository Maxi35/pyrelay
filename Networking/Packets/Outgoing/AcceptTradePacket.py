class AcceptTradePacket:
    def __init__(self):
        self.type = "ACCEPTTRADE"
        self.clientOffer = []
        self.partnerOffer = []

    def write(self, writer):
        writer.writeShort(len(self.clientOffer))
        for i in self.clientOffer:
            writer.writeBool(i)
        writer.writeShort(len(self.partnerOffer))
        for i in self.partnerOffer:
            writer.writeBool(i)

    def read(self, reader):
        offerLen = reader.readShort()
        for i in range(offerLen):
            self.clientOffer.append(reader.readBool())
        offerLen = reader.readShort()
        for i in range(offerLen):
            self.partnerOffer.append(reader.readBool())
