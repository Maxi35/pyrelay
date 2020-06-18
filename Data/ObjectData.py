from .ObjectStatusData import *

class ObjectData:
    def __init__(self, objectType=0, status=None):
        self.objectType = objectType
        if status is None:
            self.status = ObjectStatusData()
        else:
            self.status = status.clone()

    def read(self, reader):
        self.objectType = reader.readUnsignedShort()
        self.status.read(reader)

    def write(self, writer):
        writer.writeUnsignedShort(self.objectType)
        self.status.write(writer)

    def clone(self):
        return ObjectData(self.objectType, self.status.clone())

    def __str__(self):
        return "ObjectType: {}\nStatus: \n{}".format(self.objectType, self.status)
