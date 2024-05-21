from Models.PlayerData import PlayerData
from PluginManager import hook, plugin
from Constants import ClassIds

@plugin(active=True)
class PlayerTrackerPlugin:
    def __init__(self):
        self.players = {}
    
    @hook("update")
    def onUpdate(self, client, packet):
        if not client.guid in self.players:
            self.players[client.guid] = []
        for obj in packet.newObjs:
            if obj.objectType in ClassIds.ALL:
                
                pd = PlayerData()
                pd.parse(obj)
                
                self.players[client.guid].append(pd)
        
        self.players[client.guid] = [player for player in self.players[client.guid]
                                     if not player.objectId in packet.drops]
    
    @hook("mapinfo")
    def onMapInfo(self, client, packet):
        self.players[client.guid] = []
    
    @hook("newTick")
    def onNewtick(self, client, packet):
        if not client.guid in self.players:
            self.players[client.guid] = []
        for status in packet.statuses:
            for i in range(len(self.players[client.guid])):
                if self.players[client.guid][i].objectId == status.objectId:
                    self.players[client.guid][i].parseStats(status.stats)
                    self.players[client.guid][i].pos = status.pos
