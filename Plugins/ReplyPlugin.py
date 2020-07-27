from Networking.PacketHelper import CreatePacket
from PluginLoader import hook, plugin
import Models.ConditionEffect as ConditionEffect

@plugin(active=True)
class ReplyPlugin:
    def __init__(self):
        self.toReply = ""

    @hook("text")
    def onText(self, client, packet):
        if packet.name == self.toReply and packet.recipient == client.playerData.name:
            try:
                x, y = map(float, packet.text.split())
                client.nextPos = [client.pos+(x, y)]
            except ValueError:
                print("Has berserk:", ConditionEffect.hasEffect(client.playerData.condition, ConditionEffect.BERSERK))
                print("Has healing:", ConditionEffect.hasEffect(client.playerData.condition, ConditionEffect.HEALING))
                print("Has damaging:", ConditionEffect.hasEffect(client.playerData.condition, ConditionEffect.DAMAGING))
                print("Has healing or damaging:", ConditionEffect.hasEffect(client.playerData.condition, ConditionEffect.DAMAGING, ConditionEffect.HEALING))
                print()
                import time
                angle = 0
                while angle < 3.14*2:
                    if not client.isConnected():
                        return
                    if client.shoot(angle):
                        angle += 0.1
                    time.sleep(0.02)
                
    #@hook("ping")
    def onPing(self, client, packet):
        print(packet.serial)
