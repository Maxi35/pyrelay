import Data.CompressedInt as CompressedInt

class VaultUpdatePacket:
    def __init__(self):
        self.type = "VAULTUPDATE"
        self.vaultContent = []
        self.giftContent = []
        self.potionContent = []
        self.vaultUpgrageCost = -1
        self.potionUpgradeCose = -1
        self.curPotionMax = -1
        self.nextPotionMax = -1

    def read(self, reader):
        vaultCount = CompressedInt.read(reader)
        for i in range(vaultCount):
            self.vaultContent.append(CompressedInt(reader))

        giftCount = CompressedInt.read(reader)
        for i in range(giftCount):
            self.giftContent.append(CompressedInt(reader))

        potionCount = CompressedInt.read(reader)
        for i in range(potionCount):
            self.potionContent.append(CompressedInt(reader))

        self.vaultUpgrageCost = reader.readShort()
        self.potionUpgradeCose = reader.readShort()
        self.curPotionMax = reader.readShort()
        self.nextPotionMax = reader.readShort()
