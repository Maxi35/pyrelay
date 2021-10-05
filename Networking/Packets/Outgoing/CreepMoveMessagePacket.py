from Data.WorldPosData import WorldPosData


class CreepMoveMessagePacket:
    """ Sent when a summoner creep is moved """
    def __init__(self):
        self.type = "CREEPMOVEMESSAGE"
        self.objectId: int = 0  # int32
        self.position: WorldPosData = WorldPosData()  # WorldPosData
        self.hold: bool = False  # bool

    def write(self, writer):
        writer.writeInt32(self.objectId)
        self.position.write(writer)
        writer.writeBool(self.hold)

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.position.read(reader)
        self.hold = reader.readBool()
