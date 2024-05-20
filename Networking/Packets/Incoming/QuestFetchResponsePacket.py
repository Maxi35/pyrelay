from Networking.Packets.Packet import Packet
from Data.QuestData import *

class QuestFetchResponsePacket(Packet):
    def __init__(self):
        self.type = "QUESTFETCHRESPONSE"
        self.quests = []
        self.nextRefreshPrice = 0

    def read(self, reader):
        num_quests = reader.readShort()
        for i in range(num_quests):
            quest = QuestData()
            quest.read(reader)
            self.quests.append(quest)
        self.nextRefreshPrice = reader.readShort()

    def write(self, writer):
        writer.writeShort(len(self.quests))
        for quest in self.quests:
            quest.write(writer)
        writer.writeShort(self.nextRefreshPrice)
