import Networking.Packets.Incoming as Incoming
import Networking.Packets.Outgoing as Outgoing

class PacketTypes:
    def __init__(self):
        self.packet_dict = {}
        for file in dir(Incoming):
            if "Packet" in file:
                packet = getattr(Incoming, file)                
                packetName = file.replace("Packet", "")
                self.packet_dict[packetName.upper()] = packet
                
        for file in dir(Outgoing):
            if "Packet" in file:
                packet = getattr(Outgoing, file)
                packetName = file.replace("Packet", "")
                self.packet_dict[packetName.upper()] = packet
