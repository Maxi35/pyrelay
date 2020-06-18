from Networking.PacketHelper import CreatePacket

class ReplyPlugin:
    def __init__(self):
        self.toReply = ""

    def onText(self, client, packet):
        if packet.name == self.toReply or packet.recipient == client.playerData.name:
            textPacket = CreatePacket("PLAYERTEXT")
            textPacket.text = "/tell " + packet.name + " Hey"
            client.send(textPacket)

HOOKS = {"TEXT": "onText"}

INFO = {"name": "ReplyPlugin", "active": True}
