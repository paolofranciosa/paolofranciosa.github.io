import math

def eratostene_sieve(n):
    num_list = list(range(n))
    num_list[1] = 0
    div = 2
    while div*div < n:
        if num_list[div] != 0:
            for i in range(div*div, n, div):
                num_list[i] = 0
        div += 1
    primes = []
    for i in range(n):
        if num_list[i] != 0:
            primes.append(i)
    return primes

if __name__ == "__main__":
    limit = int(input("find prime less than: "))
    p = eratostene_sieve(limit)
    print("{} prime numbers less than {}:\n{}, {}, {}, ..., {}, {}, {}".format(len(p),limit, p[0],p[1],p[2],p[-3],p[-2],p[-1]))
