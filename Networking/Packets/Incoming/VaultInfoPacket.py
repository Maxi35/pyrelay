from Networking.Packets.Packet import Packet

class VaultInfoPacket(Packet):
    def __init__(self):
        self.type = "VAULTINFO"
        self.unknownBool = False
        self.chestObjectId = -1
        self.materialObjectId = -1
        self.giftObjectId = -1
        self.potionObjectId = -1
        self.spoilsObjectId = -1
        
        self.vaultContent = []
        self.materialContent = []
        self.giftContent = []
        self.potionContent = []
        self.spoilsContent = []
        self.vaultUpgrageCost = -1
        self.potionUpgradeCose = -1
        self.curPotionMax = -1
        self.nextPotionMax = -1
        self.materialUpgradeCost = -1

        self.unknownBytes = []

    def read(self, reader):
        self.unknownBool = reader.readBool()
        self.chestObjectId = reader.readCompressedInt()
        self.materialObjectId = reader.readCompressedInt()
        self.giftObjectId = reader.readCompressedInt()
        self.potionObjectId = reader.readCompressedInt()
        self.spoilsObjectId = reader.readCompressedInt()
        
        vaultCount = reader.readCompressedInt()
        for i in range(vaultCount):
            self.vaultContent.append(reader.readCompressedInt())

        materialCount = reader.readCompressedInt()
        for i in range(materialCount):
            self.materialContent.append(reader.readCompressedInt())

        giftCount = reader.readCompressedInt()
        for i in range(giftCount):
            self.giftContent.append(reader.readCompressedInt())

        potionCount = reader.readCompressedInt()
        for i in range(potionCount):
            self.potionContent.append(reader.readCompressedInt())

        spoilsCount = reader.readCompressedInt()
        for i in range(spoilsCount):
            self.spoilsContent.append(reader.readCompressedInt())
        
        self.vaultUpgrageCost = reader.readShort()
        self.materialUpgradeCost = reader.readShort()
        self.potionUpgradeCose = reader.readShort()
        self.curPotionMax = reader.readShort()
        self.nextPotionMax = reader.readShort()

        for i in range(reader.bytesAvailable()):
            self.unknownBytes.append(reader.readByte())

    def write(self, writer):
        writer.writeBool(self.unknownBool)
        writer.writeCompressedInt(self.chestObjectId)
        writer.writeCompressedInt(self.materialObjectId)
        writer.writeCompressedInt(self.giftObjectId)
        writer.writeCompressedInt(self.potionObjectId)
        writer.writeCompressedInt(self.spoilsObjectId)
        
        writer.writeCompressedInt(len(self.vaultContent))
        for i in range(len(self.vaultContent)):
            writer.writeCompressedInt(self.vaultContent[i])
        
        writer.writeCompressedInt(len(self.materialContent))
        for i in range(len(self.materialContent)):
            writer.writeCompressedInt(self.materialContent[i])
        
        writer.writeCompressedInt(len(self.giftContent))
        for i in range(len(self.giftContent)):
            writer.writeCompressedInt(self.giftContent[i])
        
        writer.writeCompressedInt(len(self.potionContent))
        for i in range(len(self.potionContent)):
            writer.writeCompressedInt(self.potionContent[i])
        
        writer.writeCompressedInt(len(self.spoilsContent))
        for i in range(len(self.spoilsContent)):
            writer.writeCompressedInt(self.spoilsContent[i])

        writer.writeShort(self.vaultUpgrageCost)
        writer.writeShort(self.materialUpgradeCost)
        writer.writeShort(self.potionUpgradeCose)
        writer.writeShort(self.curPotionMax)
        writer.writeShort(self.nextPotionMax)

        for byte in self.unknownBytes:
            writer.writeByte(byte)
