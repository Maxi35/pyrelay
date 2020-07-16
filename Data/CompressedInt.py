
def read(reader):
    value = 0
    uByte = reader.readUnsignedByte()
    isNegative = not ((uByte & 64) == 0)
    shift = 6
    value = uByte & 63;
    while uByte & 128:
        uByte = reader.readUnsignedByte()
        value = value | (uByte & 127) << shift
        shift += 7

    if isNegative:
        return -value
    
    return value
