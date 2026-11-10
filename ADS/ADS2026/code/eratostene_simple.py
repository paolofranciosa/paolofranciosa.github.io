def eratostene_sieve(n):
    '''returns the list of all primes less than n'''
    sieve = list(range(n))
    sieve[1] = 0 # number 1 is not prime by definition
    for i in range(2, n):
        if sieve[i] > 0:
            for j in range(i*i, n, i):
                sieve[j] = 0
    primes = cleaned(sieve)
    return primes
    
def all_primes(n):
    '''returns the list of all primes less than n'''
    primes_with_0_s = eratostene_sieve(n)
    primes = cleaned(primes_with_0_s)
    return primes

def cleaned(seq):
    '''returns the list of all numbers in seq different from 0'''
    return [x for x in seq if x != 0]

n = 1000
p = eratostene_sieve(n)
print(f'there are {len(p):,d} primes less than {n:,d}')
# print(p)
