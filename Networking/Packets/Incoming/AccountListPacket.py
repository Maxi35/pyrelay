from Networking.Packets.Packet import Packet

class AccountListPacket(Packet):
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

    def write(self, writer):
        writer.writeInt32(self.accountListId)
        writer.writeShort(len(self.accountIds))
        for i in range(len(self.accountIds)):
            writer.writeStr(self.accountIds[i])
        writer.writeInt32(self.lockAction)
