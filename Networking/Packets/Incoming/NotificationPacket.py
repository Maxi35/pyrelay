class NotificationPacket:
    def __init__(self):
        self.type = "NOTIFICATION"
        self.effect = 0
        self.extra = 0
        self.message = ""

        self.objectId = 0
        self.uiExtra = 0
        self.queuePos = 0
        self.color = 0
        self.pictureType = 0

    def read(self, reader):
        self.effect = reader.readByte()
        self.extra = reader.readByte()
        if self.effect == 0:#StatIncrease
            self.message = reader.readStr()
        if self.effect == 1:#ServerMessage
            self.message = reader.readStr()
        if self.effect == 2:#ErrorMessage
            self.message = reader.readStr()
        if self.effect == 3:#KeepMessage
            self.message = reader.readStr()
        if self.effect == 4:#UI
            self.message = reader.readStr()
            self.uiExtra = reader.readShort()
        if self.effect == 5:#Queue
            self.message = reader.readStr()
            self.objectId = reader.readInt32()
            self.queuePos = reader.readShort()
        if self.effect == 6:#ObjectText/json
            self.message = reader.readStr()
            self.objectId = reader.readInt32()
            self.color = reader.readInt32()
        if self.effect == 7:#Death
            self.message = reader.readStr()
            self.pictureType = reader.readInt32()
        if self.effect == 8:#DungeonOpened
            self.message = reader.readStr()
            self.pictureType = reader.readInt32()
        if self.effect == 10:#DungeonCall
            self.message = reader.readStr()
            self.unknown1 = reader.readInt32()
            self.unknown2 = reader.readByte()

    def write(self, writer):
        writer.writeByte(self.effect)
        writer.writeByte(self.extra)
        if self.effect == 0:#StatIncrease
            writer.writeStr(self.message)
        if self.effect == 1:#ServerMessage
            writer.writeStr(self.message)
        if self.effect == 2:#ErrorMessage
            writer.writeStr(self.message)
        if self.effect == 3:#KeepMessage
            writer.writeStr(self.message)
        if self.effect == 4:#UI
            writer.writeStr(self.message)
            writer.writeShort(self.uiExtra)
        if self.effect == 5:#Queue
            writer.writeStr(self.message)
            writer.writeInt32(self.objectId)
            writer.writeShort(self.queuePos)
        if self.effect == 6:#ObjectText/json
            writer.writeStr(self.message)
            writer.writeInt32(self.objectId)
            writer.writeInt32(self.color)
        if self.effect == 7:#Death
            writer.writeStr(self.message)
            writer.writeInt32(self.pictureType)
        if self.effect == 8:#DungeonOpened
            writer.writeStr(self.message)
            writer.writeInt32(self.pictureType)
        if self.effect == 10:#DungeonCall
            writer.writeStr(self.message)
            writer.writeInt32(self.unknown1)
            writer.writeByte(self.unknown2)
