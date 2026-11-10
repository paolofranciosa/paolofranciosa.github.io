def verifica_pitagorica(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def stampa_terne(max):
    x = 1
    while x <= max:
        y = x
        while y <= max:
            z = y + 1
            while z <= max:
                if verifica_pitagorica(x, y, z):
                    print("%d^2 + %d^2 = %d^2" % (x, y, z))
                z += 1
            y += 1
        x += 1

n = int(input("cerca terne pitagoriche su valori minori di ...? "))
stampa_terne(n)