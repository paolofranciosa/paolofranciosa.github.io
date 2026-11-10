import time
import random

class Sequence:
    def __init__(self, dim, max_val):
        '''creates a sequence of length dim populated by random integers
in [1, max_val]'''
        self.l = {}
        self.max_val = max_val
        for i in range(dim):
            self.l[i] = random.randint(1, max_val)

    def searches(self, l, num):
        '''performs num searches of random items in the sequence,
returns the number of successes and elapsed time'''
        start = time.time()
        tot = 0
        for i in range(num):
            val = random.randint(1, 1000000)
            if val in self.l:
                tot += 1
        return tot, time.time() - start
