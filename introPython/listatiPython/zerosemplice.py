import math

def segno(v):
    ''' restituisce il segno di un numero:
-1 se negativo,
0 se zero
+1 se positivo'''
    if v < 0:
        return -1
    elif v > 0:
        return 1
    else:
        return 0

def ricerca_zero(left, right, eps):
    '''restituisce una approssimazione dello zero di una funzione continua funz.
left e right devono essere due valori in cui la funzione assume segni discordi
eps è l'intervallo di approssimazione voluto'''
    segno_left = segno(funz(left))
    segno_right = segno(funz(right))
            
    while right - left > eps:
        print(left, right)
        med = (left + right) / 2
        if segno(funz(med)) == segno_left:
            left = med
        elif segno(funz(med)) == segno_right:
            right = med
        else:
            return med
    return (right + left) / 2

# esempio di uso della funzione ricerca_zero
def funz(x):
    return math.sin(x) - x/3

print(ricerca_zero(0.1, 3.1, 0.0000001))
