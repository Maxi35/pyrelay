import struct

class Writer:
    def __init__(self):
        self.index = 5#5 header bytes
        self.buffer = bytearray()

    def writeByte(self, value):
        self.index += 1
        self.buffer.extend(struct.pack("!b", value))

    def writeUnsignedByte(self, value):
        self.index += 1
        self.buffer.extend(struct.pack("!B", value))

    def writeInt32(self, value):
        self.index += 4
        self.buffer.extend(struct.pack("!i", value))

    def writeUInt32(self, value):
        self.index += 4
        self.buffer.extend(struct.pack("!I", value))

    def writeFloat(self, value):
        self.index += 4
        self.buffer.extend(struct.pack("!f", value))

    def writeShort(self, value):
        self.index += 2
        self.buffer.extend(struct.pack("!h", value))

    def writeUnsignedShort(self, value):
        self.index += 2
        self.buffer.extend(struct.pack("!H", value))

    def writeBool(self, value):
        self.index += 1
        self.buffer.extend(struct.pack("!?", value))
    
    def writeStr(self, string):
        if isinstance(string, str):
            string = string.encode()
        self.writeShort(len(string))
        self.index += len(string)
        self.buffer.extend(struct.pack("!{}s".format(len(string)), string))

    def writeStr32(self, string32):
        self.writeInt32(len(string32))
        if isinstance(string32, str):
            string32 = string32.encode()
        self.index += len(string32)
        self.buffer.extend(struct.pack("!{}s".format(len(string32)), string32))

    def writeBytes(self, byteList):
        self.writeShort(len(byteList))
        for byte in byteList:
            self.writeByte(byte)

    def writeCompressedInt(self, value):
        uByte = 0
        uByte |= 64*(value<0)
        value = abs(value)
        uByte |= (value&63)

        value >>= 6
        uByte |= 128*(value>0)
        
        self.writeUnsignedByte(uByte)
        
        
        while value > 0:
            uByte = value&127
            value >>= 7
            uByte |= 128*(value>0)
            self.writeUnsignedByte(uByte)

    def writeHeader(self, packetId):
        sizeBytes = struct.pack("!i", self.index)
        for idx, byte in enumerate(sizeBytes):
            self.buffer.insert(idx, byte)
        self.buffer.insert(4, packetId)

    def reset(self):
        self.index = 5
        self.buffer = bytearray()
