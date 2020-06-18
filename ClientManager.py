import random
import threading

from Client.Client import Client
from PluginLoader import callHooks
import Constants.Servers as Servers

class ClientManager:
    def __init__(self):
        self.clients = []

    def addClient(self, accInfo):
        if "guid" in accInfo.keys() and "password" in accInfo.keys():
            if not "alias" in accInfo.keys():
                accInfo["alias"] = accInfo["guid"]
            if not "server" in accInfo.keys():
                accInfo["server"] = random.choice(list(Servers.nameToIp.keys()))
                print("Server not in account info using server", accInfo["server"], "instead")
            if not accInfo["server"] in list(Servers.nameToIp.keys()):
                old = accInfo["server"]
                accInfo["server"] = random.choice(list(Servers.nameToIp.keys()))
                print("Invalid server", old, "using server", accInfo["server"], "instead")
            client = Client(accInfo)
            client.hookAllPackets(self.onPacket)
            self.clients.append(client)

    def reconnectIfNeeded(self):
        for client in self.clients:
            if not client.isConnected():
                client.connect()

    def onPacket(self, client, packet):
        callHooks(client, packet)

    def stop(self):
        print("Disconnecting clients...")
        for client in self.clients:
            client.disconnect()

"""
from ClientManager import ClientManager
from PluginLoader import loadPlugins
import json
import time

accounts = []

try:
    with open("Accounts.json", "r") as file:
        accounts = json.loads(file.read())
except IOError:
    print("Accouts.json file is missing")
    

loadPlugins()
clientMan = ClientManager()

for account in accounts:
    clientMan.addClient(account)

try:
    while 1:
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    clientMan.stop()

"""
