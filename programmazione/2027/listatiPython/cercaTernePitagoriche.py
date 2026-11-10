'''stampa tutte le terne x, y, z con x <= y < z
tali che x^2 + y^2 = z^2 '''
def verifica_pitagorica(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def stampa_terne(max):
    for x in range(max):
        for y in range(x, max):
            for z in range(y + 1, max):
                if verifica_pitagorica(x, y, z):
                    print("%d^2 + %d^2 = %d^2" % (x, y, z))

n = int(input("cerca terne pitagoriche su valori minori di ...? "))
stampa_terne(n)

