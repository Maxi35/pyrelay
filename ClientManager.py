import random
import threading

from Client.Client import Client
from PluginManager import callHooks


class ClientManager:
    def __init__(self):
        self.clients = []
        self.updateServers = False

    def addClient(self, accInfo):
        if "guid" in accInfo.keys() and "password" in accInfo.keys():
            if not "secret" in accInfo.keys():
                accInfo["secret"] = ""
            if accInfo["guid"] == "" or (accInfo["password"] == "" and accInfo["secret"] == ""):
                print("Empty email or password, skipping account")
                return False
            if not "alias" in accInfo.keys():
                accInfo["alias"] = accInfo["guid"]
            client = Client()
            client.getToken(accInfo, self.updateServers)

            import Constants.Servers as Servers
            
            if not "server" in accInfo.keys():
                accInfo["server"] = random.choice(list(Servers.nameToIp.keys()))
                print("Server not in account info using server", accInfo["server"], "instead")
            if not accInfo["server"] in list(Servers.nameToIp.keys()):
                old = accInfo["server"]
                accInfo["server"] = random.choice(list(Servers.nameToIp.keys()))
                print("Invalid server", old, "using server", accInfo["server"], "instead")
            if not "proxy" in accInfo.keys():
                accInfo["proxy"] = {}
                
            client.setup(accInfo)
            
            client.clientManager = self
            client.hookAllPackets(self.onPacket)
            self.clients.append(client)
            return True

    def removeClient(self, guid):
        new_clients = []
        for client in self.clients:
            if client.guid == guid:
                client.disconnect()
            else:
                new_clients.append(client)
        self.clients = new_clients        

    def reconnectIfNeeded(self):
        if any(client.active for client in self.clients):
            for client in self.clients:
                if client.isReady and client.active and not client.isConnected():
                    client.connect()
        else:
            return True
        
    def onPacket(self, client, packet):
        callHooks(client, packet)

    def stop(self):
        print("Disconnecting clients...")
        for client in self.clients:
            client.disconnect()
