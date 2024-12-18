from Networking.Packets.Packet import Packet

class CreatePartyPacket(Packet):
    def __init__(self):
        self.type = "CREATEPARTY"
        self.description = ""
        self.minPowerLevel = 0
        self.maxPartySize = 0
        self.activity = 0
        self.maxedStatReq = 0
        self.privacy = 0
        self.server = 0

    def write(self, writer):
        writer.writeStr(self.description)
        writer.writeShort(self.minPowerLevel)
        writer.writeByte(self.maxPartySize)
        writer.writeByte(self.activity)
        writer.writeByte(self.maxedStatReq)
        writer.writeByte(self.privacy)
        writer.writeByte(self.server)

    def read(self, reader):
        self.description = reader.readStr()
        self.minPowerLevel = reader.readShort()
        self.maxPartySize = reader.readByte()
        #0=dungeons, 1=realm, 2=other
        self.activity = reader.readByte()
        self.maxedStatReq = reader.readByte()
        #1=public, 2=private
        self.privacy = reader.readByte()
        self.server = reader.readByte()