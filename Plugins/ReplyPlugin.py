import time

from Networking.PacketHelper import CreatePacket
from PluginManager import hook, plugin

shouldEnter = False

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
            elif packet.text.lower() == "nexus":
                client.nexus()
            elif packet.text.lower() == "enter vault":
                shouldEnter = True
                replyPacket.text = f"/tell {packet.name} Entering vault..."
            else:
                replyPacket.text = f"/tell {packet.name} Unknown response"
            client.send(replyPacket)

#There can be multiple plugins in one file, be aware that all plugins
#will be used on all clients
@plugin(active=True)
class PortalPlugin:
    def __init__(self):
        self.vaultPortal = None

    @hook("ping")
    def onPing(self, client, packet):
        if shouldEnter and not self.vaultPortal is None:
            shouldEnter = False
            self.enterVault(client)
    
    #To hook a packet use the hook decorator with the packet type you wish to hook
    @hook("update")
    def onUpdate(self, client, packet):
        for e in packet.newObjs:
            if e.objectType == 1824:
                self.vaultPortal = e

    def enterVault(self, client):
        if client.pos.dist(self.vaultPortal.status.pos) < 0.5:
            usePortal = CreatePacket("USEPORTAL")
            usePortal.objectId = self.vaultPortal.status.objectId
            client.send(usePortal)
        else:
            client.nextPos = [self.vaultPortal.status.pos]
            time.sleep(0.5)
            self.enterVault(client)



