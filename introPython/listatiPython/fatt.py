def fattoriale(n):
    if n <= 1:
        return 1
    else:
        return n * fattoriale(n-1)

f = fattoriale(5)
print(f)