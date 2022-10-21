class ClientStatPacket:
    def __init__(self):
        self.type = "CLIENTSTAT"
        self.name = ""
        self.value = 0

    def read(self, reader):
        self.name = reader.readStr()
        self.value = reader.readInt32()

    def write(self, writer):
        writer.writeStr(self.name)
        writer.writeInt32(self.value)
