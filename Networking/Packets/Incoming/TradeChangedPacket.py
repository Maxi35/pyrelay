class TradeChangedPacket:
    def __init__(self):
        self.type = "TRADECHANGED"
        self.send = True
        self.offer = []

    def read(self, reader):
        offer_len = reader.readShort()
        for i in range(offer_len):
            self.offer.append(reader.readBool())

    def write(self, writer):
        writer.writeShort(len(self.offer))
        for i in range(len(self.offer)):
            writer.writeBool(self.offer[i])
