import random

n = int(input("quanti valori vuoi generare? "))
conta = 0
num_max_locali = 0
while conta < n:
    if conta == 1:
        prec = x
    elif conta > 1:
        prec_prec = prec
        prec = x
    x = random.random()
    print(x)
    if conta > 1:
        if prec_prec < prec and prec > x:
            num_max_locali += 1
    conta += 1
print("ci sono", num_max_locali, "massimi locali")
