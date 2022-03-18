class RequestTradePacket:
    def __init__(self):
        self.type = "REQUESTTRADE"
        self.name = ""

    def write(self, writer):
        writer.writeStr(self.name)

    def read(self, reader):
        self.name = reader.readStr()
