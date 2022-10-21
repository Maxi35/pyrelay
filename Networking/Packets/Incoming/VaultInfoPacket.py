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
        self.info1 = reader.readCompressedInt()
        self.chestObjectId = reader.readCompressedInt()
        self.giftObjectId = reader.readCompressedInt()
        self.potionObjectId = reader.readCompressedInt()
        
        vaultCount = reader.readCompressedInt()
        for i in range(vaultCount):
            self.vaultContent.append(reader.readCompressedInt())

        giftCount = reader.readCompressedInt()
        for i in range(giftCount):
            self.giftContent.append(reader.readCompressedInt())

        potionCount = reader.readCompressedInt()
        for i in range(potionCount):
            self.potionContent.append(reader.readCompressedInt())

        self.vaultUpgrageCost = reader.readShort()
        self.potionUpgradeCose = reader.readShort()
        self.curPotionMax = reader.readShort()
        self.nextPotionMax = reader.readShort()

    def write(self, writer):
        writer.writeCompressedInt(self.info1)
        writer.writeCompressedInt(self.chestObjectId)
        writer.writeCompressedInt(self.giftObjectId)
        writer.writeCompressedInt(self.potionObjectId)
        
        writer.writeCompressedInt(len(self.vaultContent))
        for i in range(len(self.vaultContent)):
            writer.writeCompressedInt(self.vaultContent[i])
        
        writer.writeCompressedInt(len(self.giftContent))
        for i in range(len(self.giftContent)):
            writer.writeCompressedInt(self.giftContent[i])
        
        writer.writeCompressedInt(len(self.potionContent))
        for i in range(len(self.potionContent)):
            writer.writeCompressedInt(self.potionContent[i])

        writer.writeShort(self.vaultUpgrageCost)
        writer.writeShort(self.potionUpgradeCose)
        writer.writeShort(self.curPotionMax)
        writer.writeShort(self.nextPotionMax)
