# Generare due numeri casuali nell'intervallo [0, 1),
# stamparli entrambi e stampare poi il massimo tra i due valori

import random
x = random.random()
y = random.random()
print(x, y)
print("il massimo è")
if x > y:
    print(x)
else:
    print(y)
