class AccountListPacket:
    def __init__(self):
        self.type = "ACCOUNTLIST"
        self.accountListId = 0
        self.accountIds = []
        self.lockAction = 0

    def read(self, reader):
        self.accountListId = reader.readInt32()
        accountIdsNum = reader.readShort()
        for i in range(accountIdsNum):
            self.accountIds.append(reader.readStr())
        self.lockAction = reader.readInt32()
