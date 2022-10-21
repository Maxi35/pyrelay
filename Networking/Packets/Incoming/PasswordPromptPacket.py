class PasswordPromptPacket:
    def __init__(self):
        self.type = "PASSWORDPROMPT"
        self.cleanPasswordStatus = 0

    def read(self, reader):
        self.cleanPasswordStatus = reader.readint32()

    def write(self, writer):
        writer.writeint32(self.cleanPasswordStatus)
