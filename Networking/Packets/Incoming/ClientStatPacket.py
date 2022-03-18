class ClientStatPacket:
    def __init__(self):
        self.type = "CLIENTSTAT"
        self.name = ""
        self.value = 0

    def read(self, reader):
        self.name = reader.readStr()
        self.value = reader.readInt32()
