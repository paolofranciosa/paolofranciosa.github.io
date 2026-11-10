def lista_fibonacci_ricorsiva(n):
    res = []   #  starting from an empty list
    for i in range(n):   # i ranges from 0 to n-1
        res.append(fibonacci(i))  # appends the i-th number to the List
    return res

def fibonacci(n):
    '''returns the n-th Fibonacci number'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
