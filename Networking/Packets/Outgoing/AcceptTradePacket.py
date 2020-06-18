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
