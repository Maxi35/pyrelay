class SetConditionPacket:
    def __init__(self):
        self.type = "SETCONDITION"
        self.send = True
        self.conditionEffect = 0
        self.conditionDuration = 0

    def write(self, writer):
        writer.writeByte(self.conditionEffect)
        writer.writeFloat(self.conditionDuration)

    def read(self, reader):
        self.conditionEffect = reader.readByte()
        self.conditionDuration = reader.readFloat()
