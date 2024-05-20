
class TradeItem:
    def __init__(self, item=0, slotType=0, tradeable=False, included=False, enchantment=""):
        self.item = item
        self.slotType = slotType
        self.tradeable = tradeable
        self.included = included
        self.enchantment = enchantment

    def read(self, reader):
        self.item = reader.readInt32()
        self.slotType = reader.readInt32()
        self.tradeable = reader.readBool()
        self.included = reader.readBool()
        self.enchantment = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.item)
        writer.writeInt32(self.slotType)
        writer.writeBool(self.tradeable)
        writer.writeBool(self.included)
        writer.writeStr(self.enchantment)

    def clone(self):
        return TradeItem(self.item, self.slotType, self.tradeable, self.included, self.enchantment)

    def __str__(self):
        return "Item: {}, slotType: {}, tradeable: {}, included: {}, enchantment: {}".format(self.item, self.slotType, self.tradeable, self.included, self.enchantment)

    def __repr__(self):
        return str(self.__dict__)
