from Constants.StatTypes import *
import Data.CompressedInt as CompressedInt

types = StatTypes()

class StatData:
    def __init__(self, statType=0, statValue=0, strStatValue=""):
        self.statType = statType
        self.statValue = statValue
        self.strStatValue = strStatValue

    def isStringStat(self):
        if self.statType == types.NAMESTAT:
            return True
        if self.statType == types.GUILDNAMESTAT:
            return True
        if self.statType == types.PETNAMESTAT:
            return True
        if self.statType == types.ACCOUNTIDSTAT:
            return True
        if self.statType == types.OWNERACCOUNTIDSTAT:
            return True
        return False

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
            return "StatType: {}\nValue: {}".format(self.statType, self.strStatValue)
        else:
            return "StatType: {}\nValue: {}".format(self.statType, self.statValue)

