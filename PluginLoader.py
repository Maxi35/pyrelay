import os
import importlib
import threading
import inspect

def findClass(func):#
    return getattr(inspect.getmodule(func), func.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])

class PacketHooks:
    def __init__(self):
        self._funcs = {}
        self._classes = []

    def addHook(self, packetType, func):
        if packetType in self._funcs:
            self._funcs[packetType].append(func)
        else:
            self._funcs[packetType] = [func]

    def addClass(self, cls):
        self._classes.append(cls)

    def callHooks(self, client, packet):
        if packet.type in self._funcs:
            for func in self._funcs[packet.type]:
                for cls in self._classes:
                    if type(cls) == findClass(func):
                        thread = threading.Thread(target=func, args=(cls, client, packet))
                        thread.deamon = True
                        thread.start()
        
path = "./Plugins"
import_start = "Plugins."
plugins = []
neededAttr = ["INFO"]
packetHook = PacketHooks()
loadedPlugins = []

def hook(packetType):
    def addFunc(func):
        packetHook.addHook(packetType.upper(), func)
        #return packetHook.callHooks
    return addFunc

def loadPlugins():
    for file in os.listdir(path):
        if "__" not in file and file.endswith(".py"):
            to_import = import_start + file[:-3]
            plugin = importlib.import_module(to_import)
            plugins.append(plugin)

    for plugin in plugins:
        try:
            name = plugin.INFO["name"]
            if "active" in plugin.INFO.keys():
                if not plugin.INFO["active"]:
                    print("Skipping deactivated plugin", name)
                    continue
            if name in loadedPlugins:
                print("Plugin", name, "is already loaded")
                continue
            pluginClass = getattr(plugin, name)()#Init plugin
            packetHook.addClass(pluginClass)
            print("Loading plugin", name) 
            loadedPlugins.append(name)           
        except Exception as e:
            print("Error while loading", plugin.__name__)
            print(e)

def callHooks(client, packet):
    packetHook.callHooks(client, packet)
