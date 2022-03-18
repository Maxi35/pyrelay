from Data.WorldPosData import *

class ServerPlayerShootPacket:
   def __init__(self):
      self.type = "SERVERPLAYERSHOOT"
      self.bulletId = 0
      self.ownerId = 0
      self.containerType = 0
      self.startingPos = WorldPosData()
      self.angle = 0
      self.damage = 0

   def read(self, reader):
      self.bulletId = reader.readUnsignedShort()
      self.ownerId = reader.readInt32()
      self.containerType = reader.readInt32()
      self.startingPos.read(reader)
      self.angle = reader.readFloat()
      self.damage = reader.readShort()
        
