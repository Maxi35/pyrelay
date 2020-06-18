class NameResultPacket:
    def __init__(self):
        self.type = "NAMERESULT"
        self.success = False
        self.errorText = ""

    def read(self, reader):
        self.success = reader.readBool()
        self.errorText = reader.readStr()
