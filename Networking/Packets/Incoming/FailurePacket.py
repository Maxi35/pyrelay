class FailurePacket:
    def __init__(self):
        self.type = "FAILURE"
        self.errorId = 0
        self.errorDescription = ""

    def read(self, reader):
        self.errorId = reader.readInt32()
        self.errorDescription = reader.readStr()
