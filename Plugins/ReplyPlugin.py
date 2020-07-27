from Networking.PacketHelper import CreatePacket
from PluginLoader import hook, plugin

#All plugins should have a plugin decorater
@plugin(active=True)
class ReplyPlugin:
    def __init__(self):
        self.toReply = ""

    #To hook a packet use the hook decorator with the packet type you wish to hook
    @hook("text")
    def onText(self, client, packet):
        if packet.name == self.toReply and packet.recipient == client.playerData.name:
            replyPacket = CreatePacket("PLAYERTEXT")
            if packet.text.lower() == "hello":
                replyPacket.text = f"/tell {packet.name} Hey!"
            elif packet.text.lower() == "pos":
                replyPacket.text = f"/tell {packet.name} My posision is {client.pos}"
            else:
                replyPacket.text = f"/tell {packet.name} Unknown response"
            client.send(replyPacket)
