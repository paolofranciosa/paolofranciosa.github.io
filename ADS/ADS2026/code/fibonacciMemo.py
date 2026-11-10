import time

def fib(n):
    known = {0: 0, 1: 1} # creates the initial known results dictionary
    return fast_fib(n, known)

def fast_fib(n, known):
    if n not in known:
        known[n] = fast_fib(n-1, known) + fast_fib(n-2, known)
    return known[n]

for i in range(50):
    start = time.time()
    f = fib(i)
    duration = time.time() - start
    print(f'f({i:3d}) = {f:15d} in {duration:8.3f} seconds')