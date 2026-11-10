def lista_fib_iterativa(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        ris = [0, 1]
        for i in range(2, n):
            ris.append(ris[-1] + ris[-2])
        return ris