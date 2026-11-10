import matplotlib.pyplot as plt
import math
from eratosteneAndamento import *

def cumula_inversi(n):
    s = [0] * (n)
    for i in range(1, n):
        s[i] = s[i-1] + 1/i
    return s

def grafica_armonica(n):
    fig, ax = plt.subplots()
    x = list(range(n))
    somma_inv = cumula_inversi(n)
    somma_inv_primi = [0, 0] + [somma_rec_primi(i) for i in range(2, n)]
    l = [0] + [math.log(i) for i in range(1, n)]
    ll = [0, 0] + [math.log(math.log(i)) for i in range(2, n)]
    ax.scatter(x, somma_inv)
    ax.plot(x, l)
    ax.scatter(x, somma_inv_primi)
    ax.plot(x, ll)
    plt.show()
    
if __name__ == "__main__":
    grafica_armonica(100)