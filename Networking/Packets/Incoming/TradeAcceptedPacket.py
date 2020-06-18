class TradeAcceptedPacket:
    def __init__(self):
        self.type = "TRADEACCEPTED"
        self.clientOffer = []
        self.partnerOffer = []

    def read(self, reader):
        clientOffer_len = reader.readShort()
        for i in range(clientOffer_len):
            self.clientOffer.append(reader.readBool())
        partnerOffer_len = reader.readShort()
        for i in range(partnerOffer_len):
            self.partnerOffer.append(reader.readBool())
        
