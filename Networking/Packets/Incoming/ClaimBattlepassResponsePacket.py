class ClaimBattlepassResponsePacket:
    def __init__(self):
        self.type = "CLAIMBATTLEPASSRESPONSE"
        self.send = True
        self.success = False

    def write(self, writer):
        writer.writeBool(self.success)

    def read(self, reader):
        self.success = reader.readBool()
