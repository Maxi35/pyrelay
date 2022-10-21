import struct

class Reader:
    def __init__(self):
        self.index = 5#Skip the first 5 header bytes
        self.buffer = bytearray()
        self._length = 8

    def readByte(self):
        value = struct.unpack("!b", self.buffer[self.index:self.index+1])[0]
        self.index += 1
        return value

    def readUnsignedByte(self):
        value = struct.unpack("!B", self.buffer[self.index:self.index+1])[0]
        self.index += 1
        return value

    def readInt32(self):
        value = struct.unpack("!i", self.buffer[self.index:self.index+4])[0]
        self.index += 4
        return value

    def readUInt32(self):
        value = struct.unpack("!I", self.buffer[self.index:self.index+4])[0]
        self.index += 4
        return value

    def readFloat(self):
        value = struct.unpack("!f", self.buffer[self.index:self.index+4])[0]
        self.index += 4
        return value

    def readShort(self):
        value = struct.unpack("!h", self.buffer[self.index:self.index+2])[0]
        self.index += 2
        return value

    def readUnsignedShort(self):
        value = struct.unpack("!H", self.buffer[self.index:self.index+2])[0]
        self.index += 2
        return value

    def readBool(self):
        value = struct.unpack("!?", self.buffer[self.index:self.index+1])[0]
        self.index += 1
        return value

    def readStr(self):
        strLen = self.readShort()
        string = struct.unpack("!{}s".format(strLen), self.buffer[self.index:self.index+strLen])[0]
        self.index += strLen
        if isinstance(string, bytes):
            string = string.decode()
        return string

    def readStr32(self):
        strLen = self.readInt32()
        string = struct.unpack("!{}s".format(strLen), self.buffer[self.index:self.index+strLen])[0]
        self.index += strLen
        if isinstance(string, bytes):
            string = string.decode()
        return string

    def readBytes(self):
        byteList = []
        byteListLen = self.readShort()
        for i in range(byteListLen):
            byteList.append(self.readByte())
        return byteList

    def bytesAvailable(self):
        return self._length - self.index

    def resizeAndReset(self, size):
        self.index = 5
        self.buffer = bytearray()
        self._length = size
        
