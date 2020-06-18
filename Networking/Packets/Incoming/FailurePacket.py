class FailurePacket:
    def __init__(self):
        self.type = "FAILURE"
        self.errorId = 0
        self.errorDescription = ""
        self.errorPlace = ""
        self.errorConnectionId = ""

    def read(self, reader):
        self.errorId = reader.readInt32()
        self.errorDescription = reader.readStr()
        self.errorPlace = reader.readStr()
        self.errorConnectionId = reader.readStr()
