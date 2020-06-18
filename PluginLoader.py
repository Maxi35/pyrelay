import os
import importlib
import threading

path = "./Plugins"
import_start = "Plugins."
plugins = []
neededAttr = ["INFO", "HOOKS"]
nameToHooks = {}

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
            if name in nameToHooks.keys():
                print("Plugin", name, "is already loaded")
                continue
            pluginClass = getattr(plugin, name)()
            nameToHooks[name] = [pluginClass, plugin.HOOKS]
            print("Loading plugin", name)            
        except Exception as e:
            print("Error while loading", plugin.__name__)
            print(e)

def callHooks(client, packet):
    for key in nameToHooks:
        pluginClass = nameToHooks[key][0]
        hooks = nameToHooks[key][1]
        if packet.type in hooks.keys():
            func = getattr(pluginClass, hooks[packet.type])
            thread = threading.Thread(target=func, args=(client, packet,))
            thread.deamon = True
            thread.start()
            
