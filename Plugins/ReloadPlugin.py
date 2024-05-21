from PluginManager import hook, plugin, reloadPlugins


#Reloads all plugins, keep in mind all class variables of plugins gets reset
@plugin(active=True)
class ReloadPlugin:
    def __init__(self):
        self.owner = ""

    @hook("text")
    def onText(self, client, packet):
        if packet.name == self.owner and packet.recipient == client.playerData.name:
            if packet.text.lower() == "reload":
                print("Reloading plugins...")
                reloadPlugins()
    