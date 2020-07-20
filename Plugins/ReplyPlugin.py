from Networking.PacketHelper import CreatePacket
from PluginLoader import hook

class ReplyPlugin:
    def __init__(self):
        self.toReply = "."

    @hook("text")
    def onText(self, client, packet):
        print(packet.__dict__)
        if packet.name == self.toReply or packet.recipient == client.playerData.name:
            textPacket = CreatePacket("PLAYERTEXT")
            textPacket.text = "/tell " + packet.name + " Hey"
            client.send(textPacket)

    @hook("ping")
    def onPing(self, client, packet):
        print(packet.__dict__)

INFO = {"name": "ReplyPlugin", "active": True}
