import Networking.Packets.PacketTypes as PacketTypes

packetTypes = PacketTypes.PacketTypes()

def createPacket(packetType):
    if type(packetType) != str:
        raise ValueError("Packet type have to be of type str not " + str(type(packetType)))
    packetType = packetType.upper()
    if not isValidPacket(packetType):
        raise ValueError("Invalid Packet type: " + packetType)
    return packetTypes.packet_dict[packetType]()

def isValidPacket(packetType):
    return packetType in packetTypes.packet_dict.keys()
