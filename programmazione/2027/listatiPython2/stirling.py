import math

def fattoriale(n):
    if n <= 1:
        return 1
    else:
        return n * fattoriale(n-1)

def stirling(n):
    return math.sqrt(2*math.pi*n)*(n/math.e)**n

for n in range(1,10):
    f = fattoriale(n)
    s = stirling(n)
    print(f'{n:4} {f:15d} {s:15.3f}   {f/s-1:.5f}')