from ClientManager import ClientManager
from PluginLoader import loadPlugins
from Client.Client import Client
from Helpers.Servers import update
import json
import time
import threading

#update()

accounts = []
try:
    with open("Accounts.json", "r", encoding='utf-8') as file:
        accounts = json.load(file)
except:
    print("Missing Accounts.json file")
    exit(1)
    
loadPlugins()
clientMan = ClientManager()

for account in accounts:
    thread = threading.Thread(target=clientMan.addClient, args=(account,))
    thread.deamon = True
    thread.start()

try:
    while 1:
        clientMan.reconnectIfNeeded()
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    clientMan.stop()






