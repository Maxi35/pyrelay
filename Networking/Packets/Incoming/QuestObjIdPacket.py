class QuestObjIdPacket:
    def __init__(self):
        self.type = "QUESTOBJID"
        self.objectId = 0

    def read(self, reader):
        self.objectId = reader.readInt32()
