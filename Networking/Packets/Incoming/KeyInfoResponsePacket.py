class KeyInfoResponsePacket:
    def __init__(self):
        self.type = "KEYINFORESPONSE"
        self.name = ""
        self.description = ""
        self.creator = ""

    def read(self, reader):
        self.name = reader.readStr()
        self.description = reader.readStr()
        self.creator = reader.readStr()
