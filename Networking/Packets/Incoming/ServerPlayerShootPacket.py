from Data.WorldPosData import *

class ServerPlayerShootPacket:
   def __init__(self):
      self.type = "SERVERPLAYERSHOOT"
      self.send = True
      self.bulletId = 0
      self.ownerId = 0
      self.containerType = 0
      self.startingPos = WorldPosData()
      self.angle = 0
      self.damage = 0
      self.unknownInt = 0
      self.unknownByte = 0
      self.spellBomb = False
      self.bulletCount = 0
      self.bulletAngle = 0

   def read(self, reader):
      self.bulletId = reader.readUnsignedShort()
      self.ownerId = reader.readInt32()
      self.containerType = reader.readInt32()
      self.startingPos.read(reader)
      self.angle = reader.readFloat()
      self.damage = reader.readShort()
      self.unknownInt = reader.readInt32()
      self.unknownByte = reader.readByte()
      if reader.bytesAvailable() > 0:
         self.spellBomb = True
         self.bulletCount = reader.readByte()
         self.bulletAngle = reader.readFloat()
      else:
         self.bulletCount = 0
         self.bulletAngle = 0
         
        
   def write(self, writer):
      writer.writeUnsignedShort(self.bulletId)
      writer.writeInt32(self.ownerId)
      writer.writeInt32(self.containerType)
      self.startingPos.write(writer)
      writer.writeFloat(self.angle)
      writer.writeShort(self.damage)
      writer.writeInt32(self.unknownInt)
      writer.writeByte(self.unknownByte)
      if self.spellBomb:
         writer.writeByte(self.bulletCount)
         writer.writeFloat(self.bulletAngle)
