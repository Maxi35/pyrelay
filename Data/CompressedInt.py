
def read(reader):
    value = 0
    uByte = reader.readUnsignedByte()
    isNegative = (uByte & 64) != 0
    shift = 6
    value = uByte & 63;
    while uByte & 128:
        uByte = reader.readUnsignedByte()
        value |= (uByte & 127) << shift
        shift += 7

    if isNegative:
        return -value
    
    return value
