from Networking.Packets.Packet import Packet

class MapInfoPacket(Packet):
    def __init__(self):
        self.type = "MAPINFO"
        self.width = 0
        self.height = 0
        self.name = ""
        self.displayName = ""
        self.realmName = ""
        self.seed = 0
        self.background = 0
        self.difficulty = 0
        self.allowPlayerTeleport = False
        self.showDisplays = False
        self.maxPlayers = 0
        self.gameOpenedTime = 0
        self.newBool = False
        self.buildVersion = ""
        self.newInt = 0
        self.dungeonModifiers = []
        self.unknownShort = 0
        self.maxRealmScore = 0
        self.curRealmScore = 0        

    def read(self, reader):
        self.width = reader.readInt32()
        self.height = reader.readInt32()
        self.name = reader.readStr()
        self.displayName = reader.readStr()
        self.realmName = reader.readStr()
        self.seed = reader.readUInt32()
        self.background = reader.readInt32()
        self.difficulty = reader.readFloat()
        self.allowPlayerTeleport = reader.readBool()
        self.showDisplays = reader.readBool()
        self.newBool = reader.readBool()
        self.maxPlayers = reader.readShort()
        self.gameOpenedTime = reader.readUInt32()
        self.buildVersion = reader.readStr()
        self.newInt = reader.readInt32()
        self.dungeonModifiers = reader.readStr().split(";")
        self.unknownShort = reader.readShort()#Always 0?
        if reader.bytesAvailable() == 8:
            self.maxRealmScore = reader.readInt32()
            self.curRealmScore = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.width)
        writer.writeInt32(self.height)
        writer.writeStr(self.name)
        writer.writeStr(self.displayName)
        writer.writeStr(self.realmName)
        writer.writeUInt32(self.seed)
        writer.writeInt32(self.background)
        writer.writeFloat(self.difficulty)
        writer.writeBool(self.allowPlayerTeleport)
        writer.writeBool(self.showDisplays)
        writer.writeBool(self.newBool)
        writer.writeShort(self.maxPlayers)
        writer.writeUInt32(self.gameOpenedTime)
        writer.writeStr(self.buildVersion)
        writer.writeInt32(self.newInt)
        writer.writeStr(";".join(self.dungeonModifiers))
        writer.writeShort(self.unknownShort)
        if self.maxRealmScore != 0 and self.curRealmScore != 0:
            writer.writeInt32(self.maxRealmScore)
            writer.writeInt32(self.curRealmScore)
            
