
class DamagePacket:
    def __init__(self):
        self.type = "DAMAGE"
        self.targetId = 0
        self.effects = []
        self.damageAmount = 0
        self.armorPierce = False
        self.bulletId = 0
        self.objectId = 0

    def read(self, reader):
        self.targetId = reader.readInt32()
        effectNum = reader.readUnsignedByte()
        for i in range(effectNum):
            self.effects.append(reader.readUnsignedByte())
        self.damageAmount = reader.readUnsignedShort()
        self.armorPierce = reader.readBool()
        self.bulletId = reader.readUnsignedShort()
        self.objectId = reader.readInt32()
