import random

def external_chaining_profile(dim, n):
    '''simulates n insertions at random position in a table of length dim.
Returns the frequency of the number of collisions'''
    table = [0] * dim # table[i] counts the number of items stored in position i
    for i in range(n):
        pos = random.randint(0, dim-1)
        table[pos] += 1
    return table

def frequencies(tab):
    freq = dict()
    for c in tab:
        freq[c] = freq.get(c, 0) + 1
    return freq

if __name__ == "__main__":
    n   = 1000000
    dim = 13000
    print(f'{n} insertions in {dim} positions:')
    t = external_chaining_profile(dim, n)
    distr = frequencies(t)
    for c in sorted(distr.keys()):
        print(f'{c:4d}: {distr[c]:4d}')