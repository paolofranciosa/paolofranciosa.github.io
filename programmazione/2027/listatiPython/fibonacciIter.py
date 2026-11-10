def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pprec = 0
        prec = 1
        fib = 1
        k = 2
        while k < n:
            pprec = prec
            prec = fib
            fib = pprec + prec
            k += 1
        return fib
    

for i in range(2,45):
    print(f'f({i:2d}) = {fibonacci(i):10} rapp ={fibonacci(i)/fibonacci(i-1):15.13f}')
            