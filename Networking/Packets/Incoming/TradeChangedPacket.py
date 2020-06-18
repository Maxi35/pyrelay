class TradeChangedPacket:
    def __init__(self):
        self.type = "TRADECHANGED"
        self.offer = []

    def read(self, reader):
        offer_len = reader.readShort()
        for i in range(offer_len):
            self.offer.append(reader.readBool())
