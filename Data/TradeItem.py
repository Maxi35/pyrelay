
class TradeItem:
    def __init__(self, item=0, slotType=0, tradeable=False, included=False):
        self.item = item
        self.slotType = slotType
        self.tradeable = tradeable
        self.included = included

    def read(self, reader):
        self.item = reader.readInt32()
        self.slotType = reader.readInt32()
        self.tradeable = reader.readBool()
        self.included = reader.readBool()

    def write(self, writer):
        writer.writeInt32(self.item)
        writer.writeInt32(self.slotType)
        writer.writeBool(self.tradeable)
        writer.writeBool(self.included)

    def clone(self):
        return TradeItem(self.item, self.slotType, self.tradeable, self.included)

    def __str__(self):
        return "Item: {}, slotType: {}, tradeable: {}, included: {}".format(self.item, self.slotType, self.tradeable, self.included)

    def __repr__(self):
        return str(self.__dict__)
