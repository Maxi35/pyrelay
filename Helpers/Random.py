
class Random:
    def __init__(self, seed=0):
        self.seed = seed

    def nextInt(self, min, max):
        if min == max:
            return min
        return min + self.generate() % (max-min)

    def generate(self):
        lo = 16807 * (self.seed & 65535)
        hi = 16807 * (self.seed >> 16)
        lo += (hi & 32767) << 16
        lo += hi >> 15
        if lo > 2147483647:
            lo -= 2147483647
        self.seed = lo
        return self.seed

    def setSeed(self, seed):
        self.seed = seed
