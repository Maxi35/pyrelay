import Data.CompressedInt as CompressedInt

class VaultInfoPacket:
    def __init__(self):
        self.type = "VAULTINFO"
        self.info1 = -1
        self.chestObjectId = -1
        self.giftObjectId = -1
        self.potionObjectId = -1
        
        self.vaultContent = []
        self.giftContent = []
        self.potionContent = []
        self.vaultUpgrageCost = -1
        self.potionUpgradeCose = -1
        self.curPotionMax = -1
        self.nextPotionMax = -1

    def read(self, reader):
        self.info1 = CompressedInt.read(reader)
        self.chestObjectId = CompressedInt.read(reader)
        self.giftObjectId = CompressedInt.read(reader)
        self.potionObjectId = CompressedInt.read(reader)
        
        vaultCount = CompressedInt.read(reader)
        for i in range(vaultCount):
            self.vaultContent.append(CompressedInt.read(reader))

        giftCount = CompressedInt.read(reader)
        for i in range(giftCount):
            self.giftContent.append(CompressedInt.read(reader))

        potionCount = CompressedInt.read(reader)
        for i in range(potionCount):
            self.potionContent.append(CompressedInt.read(reader))

        self.vaultUpgrageCost = reader.readShort()
        self.potionUpgradeCose = reader.readShort()
        self.curPotionMax = reader.readShort()
        self.nextPotionMax = reader.readShort()
