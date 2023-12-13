from Constants.StatTypes import *

types = StatTypes()

class StatData:
    def __init__(self, statType=0, statValue=0, strStatValue="", secondaryValue=0):
        self.statType = statType
        self.statValue = statValue
        self.strStatValue = strStatValue
        self.secondaryValue = secondaryValue

    def isStringStat(self):
        return self.statType in [types.EXPSTAT, types.NAMESTAT, types.ACCOUNTIDSTAT, types.GUILDNAMESTAT,
                                 types.PETNAMESTAT, types.GRAVEACCOUNTID, types.OWNERACCOUNTIDSTAT,
                                 types.UNKNOWN80, types.UNKNOWN121, types.ENCHANTMENT, types.UNKNOWN128,
                                 types.UNKNOWN147]

    def statToName(self, type=None):
        if type is None:
            return types.nameOf(self.statType)
        else:
            return types.nameOf(type)   

    def read(self, reader):
        self.statType = reader.readUnsignedByte()
        if self.isStringStat():
            self.strStatValue = reader.readStr()
        else:
            self.statValue = reader.readCompressedInt()
        self.secondaryValue = reader.readCompressedInt()

    def write(self, writer):
        writer.writeUnsignedByte(self.statType)
        if self.isStringStat():
            writer.writeStr(self.strStatValue)
        else:
            writer.writeCompressedInt(self.statValue)
        writer.writeCompressedInt(self.secondaryValue)

    def clone(self):
        return StatData(self.statType, self.statValue, self.strStatValue, self.secondaryValue)

    def __str__(self):
        if self.isStringStat():
            return "statType: {}\nstrStatValue: {}\nsecondaryValue: {}".format(self.statType, self.strStatValue, self.secondaryValue)
        else:
            return "statType: {}\nstatValue: {}\nsecondaryValue: {}".format(self.statType, self.statValue, self.secondaryValue)

