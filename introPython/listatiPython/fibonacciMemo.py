fibs = {0:0, 1:1}
def fib(n):
    if n in fibs:
        return fibs[n]
    else:
        fibs[n] = fib(n-1) + fib(n-2)
        return fibs[n]

if __name__ == "__main__": # chiamata di prova
    print(fib(20))