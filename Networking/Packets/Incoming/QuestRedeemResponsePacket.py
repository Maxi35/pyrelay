class QuestRedeemResponsePacket:
    def __init__(self):
        self.type = "QUESTREDEEMRESPONSE"
        self.ok = False
        self.message = ""

    def read(self, reader):
        self.ok = reader.readBool()
        self.message = reader.readStr()
