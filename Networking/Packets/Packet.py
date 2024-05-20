class Packet:
    send = True
    def __init__(self):
        pass
    
    def read(self, reader):
        pass
    
    def write(self, writer):
        pass

    def __str__(self):
        return str(self.__dict__)