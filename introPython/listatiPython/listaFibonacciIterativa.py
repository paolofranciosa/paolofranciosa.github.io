def lista_fibonacci_iterativa(n):
    '''calcolo iterativo dei primi n elementi della sequenza di Fibonacci.
Molto efficiente, richiede un numero di operazioni lineari in n,
assumento che la somma di due naturali sia una sola operazione.'''
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i-1] + res[i-2])
    return res

