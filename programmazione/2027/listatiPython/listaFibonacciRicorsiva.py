def lista_fibonacci_ricorsiva(n):
    res = []
    for i in range(n):
        res.append(fibonacci(i))
    return res

def fibonacci(n):
    '''restituisce l'n-esimno numero di Fibonacci'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

