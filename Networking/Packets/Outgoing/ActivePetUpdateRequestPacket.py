class ActivePetUpdateRequestPacket:
    def __init__(self):
        self.type = "ACTIVEPETUPDATEREQUEST"
        self.commandType = 0
        self.instanceId = 0

    def write(self, writer):
        writer.writeByte(self.commandType)
        writer.writeInt32(self.instanceId)
