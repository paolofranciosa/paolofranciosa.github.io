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

def ricerca_zero(f, left, right, eps):
    '''restituisce una approssimazione dello zero di una funzione continua.
f e' una funzione continua
left e right devono essere due valori in cui la funzione assume segni discordi
eps e' l'intervallo di approssimazione voluto'''
    segno_left = segno(f(left))
    segno_right = segno(f(right))
            
    while right - left > eps:
        print(f'left: {left:18.15f} right: {right:18.15f}')
        med = (left + right) / 2
        if segno(f(med)) == segno_left:
            left = med
        elif segno(f(med)) == segno_right:
            right = med
        else:
            return med
    return (right + left) / 2

# esempio di uso della funzione ricerca_zero
def funz(x):
    return math.sin(x) - x/3

print(ricerca_zero(funz, 0.1, 3.1, 0.0000001))
