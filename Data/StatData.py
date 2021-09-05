from Constants.StatTypes import *
import Data.CompressedInt as CompressedInt

types = StatTypes()

class StatData:
    def __init__(self, statType=0, statValue=0, strStatValue="", secondaryValue=0):
        self.statType = statType
        self.statValue = statValue
        self.strStatValue = strStatValue
        self.secondartValue = secondaryValue

    def isStringStat(self):
##        return self.statType in [31, 62, 82, 38, 54, 115, 25, 69, 122]
        return self.statType in [types.NAMESTAT, types.ACCOUNTIDSTAT, types.GUILDNAMESTAT,
                                 types.PETNAMESTAT, types.GRAVEACCOUNTID, types.OWNERACCOUNTIDSTAT,
                                 types.UNKNOWN80, types.UNKNOWN121, types.UNKNOWN123]
##        return self.statType in [types.NAMESTAT, types.GUILDNAMESTAT, types.PETNAMESTAT,
##                                 types.ACCOUNTIDSTAT, types.OWNERACCOUNTIDSTAT, types.GRAVEACCOUNTID,
##                                 types.UNKNOWN80, types.UNKNOWN121, types.UNKNOWN123]

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
            self.statValue = CompressedInt.read(reader)
        secondaryValue = CompressedInt.read(reader)

    def write(self, writer):
        writer.writeUnsignedByte(self.statType)
        if self.isStringStat():
            writer.writeStr(self.strStatValue)
        else:
            writer.writeInt32(self.statValue)

    def clone(self):
        return StatData(self.statType, self.statValue, self.strStatValue)

    def __str__(self):
        if self.isStringStat():
            return "statType: {}\nstrStatValue: {}".format(self.statType, self.strStatValue)
        else:
            return "statType: {}\nstatValue: {}".format(self.statType, self.statValue)

