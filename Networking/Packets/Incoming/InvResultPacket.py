class InvResultPacket:
    def __init__(self):
        self.type = "INVRESULT"
        self.result = 0
    
    def read(self, reader):
        self.result = reader.readInt32()
