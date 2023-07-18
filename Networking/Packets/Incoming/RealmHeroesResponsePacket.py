class RealmHeroesResponsePacket:
    def __init__(self):
        self.type = "REALMHEROESRESPONSE"
        self.send = True
        self.numberOfRealmHeros = 0

    def read(self, reader):
        self.numberOfRealmHeros = reader.readInt32()

    def write(self, writer):
        writer.writeInt32(self.numberOfRealmHeros)
