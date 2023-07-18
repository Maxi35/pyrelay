class Unknown121Packet:
    def __init__(self):
        self.type = "UNKNOWN121"#Always sent after ability?
        self.send = True
        self.time = 0
        self.unknownShort = 0

    def write(self, writer):
        writer.writeInt32(self.time)
        writer.writeShort(self.unknownShort)

    def read(self, reader):
        self.time = reader.readInt32()
        self.unknownShort = reader.readShort()#Alwasy 1?
