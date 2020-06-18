
class SlotObjectData:
    def __init__(self, objectId=0, slotId=0, objectType=0):
        self.objectId = objectId
        self.slotId = slotId
        self.objectType = objectType

    def read(self, reader):
        self.objectId = reader.readInt32()
        self.slotId = reader.readUnsignedByte()
        self.objectType = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.objectId)
        writer.writeUnsignedByte(self.slotId)
        writer.writeInt32(self.objectType)

    def clone(self):
        return SlotObjectData(self.objectId, self.slotId, self.objectType)
        
