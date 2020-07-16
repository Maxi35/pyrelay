class ChangeTradePacket:
    def __init__(self):
        self.type = "CHANGETRADE"
        self.offer = []

    def write(self, writer):
        writer.writeShort(len(self.offer))
        for i in self.offer:
            writer.writeBool(i)