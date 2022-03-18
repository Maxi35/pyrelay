import os
import importlib
import threading
import inspect
from Networking.PacketHelper import isValidPacket

def findClass(func):
    return getattr(inspect.getmodule(func), func.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0])

class PacketHooks:
    def __init__(self):
        self._funcs = {}
        self._classes = []

    def addHook(self, packetType, func):
        if isValidPacket(packetType.upper()):
            if packetType in self._funcs:
                self._funcs[packetType].append(func)
            else:
                self._funcs[packetType] = [func]
        else:
            print("WARNING: hooked packet", packetType, "is not a valid packet type")

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

class Plugins:
    def __init__(self):
        self._plugins = []

    def addPlugin(self, plugin, args, options):
        if options["active"]:
            self._plugins.append(plugin)
        else:
            print("Skipping deactivated plugin", plugin.__module__.replace("Plugins.","",1) + "." + plugin.__name__)

    def getPlugins(self):
        return self._plugins

path = "./Plugins"
import_start = "Plugins."
packetHook = PacketHooks()
plugins = Plugins()

def hook(packetType):
    def addFunc(func):
        packetHook.addHook(packetType.upper(), func)
        return func
    return addFunc

def plugin(*args, **kwargs):
    def addPlugin(pluginClass):
        plugins.addPlugin(pluginClass, args, kwargs)
        return pluginClass
    return addPlugin

def loadPlugins():
    for file in os.listdir(path):
        if "__" not in file and file.endswith(".py"):
            to_import = import_start + file[:-3]
            importlib.import_module(to_import)

    for pluginClass in plugins.getPlugins():
        try:
            cls = pluginClass()#Init plugin
            packetHook.addClass(cls)
            print("Loaded plugin", pluginClass.__module__.replace("Plugins.","",1) + "." + pluginClass.__name__)
        except Exception as e:
            print("Error while loading", pluginClass.__name__)
            print(e)

def callHooks(client, packet):
    packetHook.callHooks(client, packet)
