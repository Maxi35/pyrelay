class ClaimDailyRewardResponsePacket:
    def __init__(self):
        self.type = "CLAIMDAILYREWARDRESPONSE"
        self.itemId = 0
        self.quantity = 0
        self.gold = 0

    def read(self, reader):
        self.itemId = reader.readInt32()
        self.quantity = reader.readInt32()
        self.gold = reader.readInt32()
