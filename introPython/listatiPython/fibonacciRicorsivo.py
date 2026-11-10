import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

for i in range(2,37):
    inizio = time.time()
    num = fibonacci(i)
    durata = time.time() - inizio
    print(f'f({i:2d}) = {num:12} in {durata:15.6f} secondi')
            