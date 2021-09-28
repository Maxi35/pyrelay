import Networking.Packets.Incoming as Incoming
import Networking.Packets.Outgoing as Outgoing

class PacketTypes:
    def __init__(self):
        for file in dir(Incoming):
            if "Packet" in file:
                file = file.replace("Packet", "")
                self.__dict__[file.upper()] = file.upper()
        for file in dir(Outgoing):
            if "Packet" in file:
                file = file.replace("Packet", "")
                self.__dict__[file.upper()] = file.upper()
