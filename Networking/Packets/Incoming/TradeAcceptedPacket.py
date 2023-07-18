class TradeAcceptedPacket:
    def __init__(self):
        self.type = "TRADEACCEPTED"
        self.send = True
        self.clientOffer = []
        self.partnerOffer = []

    def read(self, reader):
        clientOffer_len = reader.readShort()
        for i in range(clientOffer_len):
            self.clientOffer.append(reader.readBool())
        partnerOffer_len = reader.readShort()
        for i in range(partnerOffer_len):
            self.partnerOffer.append(reader.readBool())
        
    def writer(self, writer):
        writer.writeShort(len(self.clientOffer))
        for i in range(len(self.clientOffer)):
            writer.writeBool(self.clientOffer[i])
        writer.writeShort(len(self.partnerOffer))
        for i in range(len(self.partnerOffer)):
            writer.writeBool(self.partnerOffer[i])
