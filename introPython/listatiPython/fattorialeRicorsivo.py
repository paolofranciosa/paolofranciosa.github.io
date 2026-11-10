def fattoriale(n):
    if n < 2:
        return 1
    else:
        return n * fattoriale(n-1)


ris = fattoriale(4)
print(ris)