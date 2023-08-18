from Data.FameData import *

class DeathPacket:
    def __init__(self):
        self.type = "DEATH"
        self.send = True
        self.accountId = ""
        self.charId = 0
        self.killedBy = ""
        self.unknownInt = 0
        self.fameEarned = 0
        self.fameBonuses = []
        self.PCStats = ""

    def read(self, reader):
        self.accountId = reader.readStr()
        self.charId = reader.readCompressedInt()
        self.killedBy = reader.readStr()
        self.unknownInt = reader.readInt32()
        self.fameEarned = reader.readCompressedInt()
        fameBonuses = reader.readCompressedInt()
        for i in range(fameBonuses):
            fameData = FameData()
            fameData.read(reader)
            self.fameBonuses.append(fameData)
        self.PCStats = reader.readStr()
        

    def write(self, writer):
        writer.writeStr(self.accountId)
        writer.writeCompressedInt(self.charId)
        writer.writeStr(self.killedBy)
        writer.writeInt32(self.unknownInt)
        writer.writeCompressedInt(self.fameEarned)
        writer.writeCompressedInt(len(self.fameBonuses))
        for fameData in self.fameBonuses:
            fameData.write(writer)
        writer.writeStr(self.PCStats)
