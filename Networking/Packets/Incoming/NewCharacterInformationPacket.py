class NewCharacterInformationPacket:
    def __init__(self):
        self.type = "NEWCHARACTERINFORMATION"
        self.charXML = ""

    def read(self, reader):
        self.charXML = reader.readStr()

    def write(self, writer):
        write.writeStr(self.charXML)
