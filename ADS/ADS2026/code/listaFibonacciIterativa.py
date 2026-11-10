def lista_fibonacci_iterativa(n):
    '''returns the sequence of the first n Fibonacci numbers.
The complexity is linear in n,
assuming that two numbers can be summed in constant time.'''
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i-1] + res[i-2])
    return res
