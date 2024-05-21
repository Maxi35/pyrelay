
class QuestData:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.description = ""
        self.expiration = ""
        self.category = 0
        self.type = 0#<7 = quest tab, 7 = event tab
        self.itemsNeeded = []
        self.rewards = []
        self.completed = False
        self.choice = False
        self.repeatable = False

    def read(self, reader):
        self.id = reader.readStr()
        self.name = reader.readStr()
        self.description = reader.readStr()
        self.expiration = reader.readStr()
        self.category = reader.readInt32()
        self.type = reader.readInt32()

        num_items_needed = reader.readShort()
        for i in range(num_items_needed):
            self.itemsNeeded.append(reader.readInt32())
            
        num_rewards = reader.readShort()
        for i in range(num_rewards):
            self.rewards.append(reader.readInt32())

        self.completed = reader.readBool()
        self.choice = reader.readBool()
        self.repeatable = reader.readBool()

    def write(self, writer):
        writer.writeStr(self.id)
        writer.writeStr(self.name)
        writer.writeStr(self.description)
        writer.writeStr(self.expiration)
        writer.writeInt32(self.category)
        writer.writeInt32(self.type)
        
        writer.writeShort(len(self.itemsNeeded))
        for item in self.itemsNeeded:
            writer.writeInt32(item)
            
        writer.writeShort(len(self.rewards))
        for reward in self.rewards:
            writer.writeInt32(reward)
        
        writer.writeBool(self.completed)
        writer.writeBool(self.choice)
        writer.writeBool(self.repeatable)
