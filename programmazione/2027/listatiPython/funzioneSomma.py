# definizione di una funzione che accetta due parametri e
# restituisce la loro somma

def somma(x, y):
    risultato = x + y
    return risultato


# esempi di uso della funzione

print(somma(3, 2) * somma(2, 1))

a = int(input("scrivi un numero: "))
b = int(input("scrivi un altro numero: "))
print("la somma dei due numeri e'", somma(a, b))
