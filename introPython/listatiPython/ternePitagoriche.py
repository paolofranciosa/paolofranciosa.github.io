def massimo(x, y, z):
    m = x
    if y > m:
        m = y
    if z > m:
        m = z
    return m

def minimo(x, y, z):
    m = x
    if y < m:
        m = y
    if z < m:
        m = z
    return m

# funzione che, dati tre numeri,
# decide se e' una terna pitagorica
def pitagorica(a, b, c):
    massimo_dei_tre = massimo(a, b, c)
    minimo_dei_tre = minimo(a, b, c)
    mediano_dei_tre = (a + b + c) - (massimo_dei_tre + minimo_dei_tre)
    if massimo_dei_tre**2 == minimo_dei_tre**2 + mediano_dei_tre**2:
        return True
    else:
        return False

# ciascuna delle chiamate nel seguito restituisce True o False
# quindi le print stamperanno il valore True o False
# ci si aspetta che la sequenza di print sia
# True True True False False
print(pitagorica(3,4,5))
print(pitagorica(5,4,3))
print(pitagorica(3,5,4))
print(pitagorica(3,4,6))
print(pitagorica(5,4,5))
