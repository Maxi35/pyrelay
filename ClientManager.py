import random
from hashlib import md5
from Client.Client import Client

class ClientManager:
    def __init__(self):
        self.clients = []
        self.updateServers = False
        self.baseAccInfo = {"guid": "", "password": "", "secret": ""}

    def addClient(self, accInfo):
        accInfo = self.baseAccInfo | accInfo

        if accInfo["guid"] == "" or (accInfo["password"] == "" and accInfo["secret"] == ""):
            print("Empty email or password/secret, skipping account")
            return None
        if not "alias" in accInfo.keys():
            accInfo["alias"] = accInfo["guid"]
        if "proxy" in accInfo.keys():
            if not "username" in accInfo["proxy"].keys():
                accInfo["proxy"]["username"] = ""
            if not "password" in accInfo["proxy"].keys():
                accInfo["proxy"]["password"] = ""
                
        for client in self.clients:
            if client.guid == accInfo["guid"]:
                print("Account already added")
                return None
            
        proxy  = accInfo.get("proxy", {})
        proxies = {}
        if proxy != {}:
            proxies = {
                    "https": "socks{}://".format(proxy["type"]) +
                    ("{}:{}@".format(proxy["username"], proxy["password"]) if proxy["username"] != "" else "") +
                    "{}:{}".format(proxy["host"], proxy["port"])
                    }
            
        client = Client()
        
        client.clientToken = md5(accInfo["guid"].encode("utf-8") + accInfo["password"].encode("utf-8")).hexdigest()
        client.proxies = proxies
        
        client.getToken(accInfo)
        
        client.checkInfo(accInfo, self.updateServers)

        import Constants.Servers as Servers
        
        if not "server" in accInfo.keys():
            accInfo["server"] = random.choice(list(Servers.nameToIp.keys()))
            print("Server not in account info using server", accInfo["server"], "instead")
        if not accInfo["server"] in list(Servers.nameToIp.keys()):
            old = accInfo["server"]
            accInfo["server"] = random.choice(list(Servers.nameToIp.keys()))
            print("Invalid server", old, "using server", accInfo["server"], "instead")
            
        client.setup(accInfo)
        
        client.clientManager = self
        client.connect()
        
        self.clients.append(client)
        
        return client

    def removeClient(self, guid):
        new_clients = []
        for client in self.clients:
            if client.guid == guid:
                client.stop()
            else:
                new_clients.append(client)
        self.clients = new_clients        

    def reconnectIfNeeded(self):
        if any(client.active for client in self.clients):
            for client in self.clients:
                if client.isReady and client.active and not client.isConnected():
                    #Has client been disconnected for more than 2.5 secs?
                    if client.lastPacketTime + 2500 < client.getTime():
                        client.connect()
        else:
            return True

    def stop(self):
        print("Disconnecting clients...")
        for client in self.clients:
            client.stop()
