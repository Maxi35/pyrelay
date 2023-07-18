from Data.TradeItem import*

class TradeStartPacket:
    def __init__(self):
        self.type = "TRADESTART"
        self.send = True
        self.clientItems = []
        self.partnerName = ""
        self.partnerItems = []

    def read(self, reader):
        clientItems_len = reader.readShort()
        for i in range(clientItems_len):
            item = TradeItem()
            item.read(reader)
            self.clientItems.append(item)
        self.partnerName = reader.readStr()
        partnerItems_len = reader.readShort()
        for i in range(partnerItems_len):
            item = TradeItem()
            item.read(reader)
            self.partnerItems.append(item)

    def write(self, writer):
        writer.writeShort(len(self.clientItems))
        for i in range(len(self.clientItems)):
            self.clientItems[i].write(writer)
        writer.writeStr(self.partnerName)
        writer.writeShort(len(self.partnerItems))
        for i in range(len(self.partnerItems)):
            self.partnerItems[i].write(writer)
