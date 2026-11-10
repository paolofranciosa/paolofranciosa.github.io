import math

def fattoriale(n):
    fatt = 1
    for i in range(1, n+1):
        fatt = fatt * i
    return fatt

def fattoriale_Stirling(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n    

for n in range(10, 31):
    print(n, float(fattoriale(n)), fattoriale_Stirling(n))
print()
for n in range(10, 51, 5):
    print(n, fattoriale(n) / fattoriale_Stirling(n))