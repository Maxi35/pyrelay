OUTGOING_KEY = "5a4d2016bc16dc64883194ffd9"
INCOMING_KEY = "c91d9eec420160730d825604e0"
STATE_LENGTH = 256

class RC4:
    def __init__(self, key):
        self.key = bytearray.fromhex(key)
        self.x = 0
        self.y = 0
        self.state = [0] * STATE_LENGTH
        self.reset()

    def process(self, data):
        if isinstance(data, str):
            data = bytearray.fromhex(data)
        elif isinstance(data, bytes):
            data = bytearray(data)
        for i in range(len(data)):
            self.x = (self.x + 1) % STATE_LENGTH
            self.y = (self.y + self.state[self.x]) % STATE_LENGTH
            self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]
            k = self.state[(self.state[self.x] + self.state[self.y]) % STATE_LENGTH]
            data[i] = data[i] ^ k
        return data

    def reset(self):
        self.x = 0
        self.y = 0
        for i in range(STATE_LENGTH):
            self.state[i] = i
        i2 = 0
        for i in range(STATE_LENGTH):
            i2 = (i2 + self.state[i] + self.key[i%len(self.key)]) % STATE_LENGTH
            self.state[i], self.state[i2] = self.state[i2], self.state[i]
 
