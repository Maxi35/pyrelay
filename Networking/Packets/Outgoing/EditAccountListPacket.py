class EditAccountListPacket:
    def __init__(self):
        self.type = "EDITACCOUNTLIST"
        self.send = True
        self.accountListId = 0
        self.add = False
        self.objectId = 0

    def write(self, writer):
        writer.writeInt32(self.accountListId)
        writer.writeBool(self.add)
        writer.writeInt32(self.objectId)

    def read(self, reader):
        self.accountListId = reader.readInt32()
        self.add = reader.readBool()
        self.objectId = reader.readInt32()
