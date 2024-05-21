import os
import sys
import importlib
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
                        if type(cls) == type(client):
                            func(client, packet)
                        else:
                            func(cls, client, packet)

    def resetPlugins(self):
        #Remove all plugin hooks and classes, but keep client hooks and classes
        new_funcs = {}
        for packetType in self._funcs:
            hooks = []
            for func in self._funcs[packetType]:
                if "Client." in str(func):
                    hooks.append(func)
            if len(hooks) > 0:
                new_funcs[packetType] = hooks
        self._funcs = new_funcs
            
        self._classes = [c for c in self._classes 
                         if "Client.Client" in str(type(c))]

class Plugins:
    def __init__(self):
        self._plugins = []

    def addPlugin(self, plugin, args, options):
        if options["active"]:
            self._plugins.append(plugin)
        else:
            print("Skipping deactivated plugin", plugin.__module__.replace("Plugins.","",1) + "." + plugin.__name__)

    def reset(self):
        for p in self._plugins:
            if p.__module__ in sys.modules:
                del sys.modules[p.__module__]
            del p
        self._plugins = []

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

def client():
    def addClient(clientClass):
        packetHook.addClass(clientClass())
        return clientClass
    return addClient

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

def reloadPlugins():
    packetHook.resetPlugins()
    plugins.reset()
    loadPlugins()

def callHooks(client, packet):
    packetHook.callHooks(client, packet)
