import random

tabella = []
for i in range(4):
    tabella.append([])
    for j in range(7):
        tabella[i].append(random.random())
mat = tabella

for riga in mat:
    for elem in riga:
        print(elem, end = " ")
    print()

for riga in mat:
    for elem in riga:
        print("%.4f  " % elem, end = "")
    print()
