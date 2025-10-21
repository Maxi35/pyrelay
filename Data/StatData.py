from Constants.StatTypes import StatTypes, nameOf

class StatData:
    def __init__(self, statType=0, statValue=0, strStatValue="", secondaryValue=0):
        self.statType = statType
        self.statValue = statValue
        self.strStatValue = strStatValue
        self.secondaryValue = secondaryValue

    def isStringStat(self):
        return self.statType in [StatTypes.EXPSTAT, StatTypes.NAMESTAT, StatTypes.ACCOUNTIDSTAT, StatTypes.GUILDNAMESTAT,
                                StatTypes.PETNAMESTAT, StatTypes.GRAVEACCOUNTID, StatTypes.OWNERACCOUNTIDSTAT,
                                StatTypes.ENCHANTMENTS, StatTypes.UNKNOWN121, StatTypes.MATERIALAMOUNTSTAT, StatTypes.CRUCIBLESTAT,
                                StatTypes.DUSTCAPSTAT, StatTypes.DUSTAMOUNTSTAT, StatTypes.MATERIALCAPSTAT, StatTypes.UNKNOWN155]

    def statToName(self, statType=None):
        if statType is None:
            return nameOf(self.statType)
        else:
            return nameOf(statType)   

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

