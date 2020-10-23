
class SlotObjectData:
    def __init__(self, objectId=0, slotId=0, objectType=0):
        self.objectId = objectId
        self.slotId = slotId
        self.objectType = objectType

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.slotId = reader.readInt32()
        self.objectType = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.objectId)
        writer.writeInt32(self.slotId)
        writer.writeInt32(self.objectType)

    def __str__(self):
        return "{} {} {}".format(self.objectId, self.slotId, self.objectType)

    def clone(self):
        return SlotObjectData(self.objectId, self.slotId, self.objectType)
        
