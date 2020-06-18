class RealmHeroesResponsePacket:
    def __init__(self):
        self.type = "REALMHEROESRESPONSE"
        self.numberOfRealmHeros = 0

    def read(self, reader):
        self.numberOfRealmHeros = reader.readInt32()
