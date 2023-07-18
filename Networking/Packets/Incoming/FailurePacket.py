class FailurePacket:
    def __init__(self):
        self.type = "FAILURE"
        self.send = True
        self.errorId = 0
        self.errorDescription = ""

    def read(self, reader):
        self.errorId = reader.readInt32()
        self.errorDescription = reader.readStr()

    def write(self, writer):
        writer.writeInt32(self.errorId)
        writer.writeStr(self.errorDescription)
