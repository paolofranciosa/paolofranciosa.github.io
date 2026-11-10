# siano (px, py), (qx, qy)  i punti che definiscono un rettangolo
# con gli assi paralleli agli assi cartesiani, con  px < qx  e  py < qy
# sia inoltre (cx, cy) il centro di un cerchio, ed r il suo raggio
# Si assume che r non sia mai negativo
#
# scrivere una funzione che dati come parametri px, py, qx, qy, cx, cy, r
# restituisce True se il cerchio e' contenuto nel rettangolo e
# restituisce False altrimenti

# e' decisamente piu' complicato scrivere una funzione che determina
# se le due figure si intersecano ....


def cerchio_in_rettangolo(.....):
    ....


# esempi di uso
print(cerchio_in_rettangolo(0, 0, 10, 20, 5, 5, 4))
print("la chiamata precedente dovrebbe restituire True\n")
print(cerchio_in_rettangolo(0, 0, 10, 20, 6, 5, 7))
print("la chiamata precedente dovrebbe restituire False\n")
print(cerchio_in_rettangolo(0, 0, 20, 10, 15, 4, 3))
print("la chiamata precedente dovrebbe restituire True\n")
print(cerchio_in_rettangolo(0, 0, 20, 10, 30, 30, 1))
print("la chiamata precedente dovrebbe restituire False\n")
print(cerchio_in_rettangolo(0, 0, 20, 10, 30, 30, 1))
print("la chiamata precedente dovrebbe restituire False\n")
print(cerchio_in_rettangolo(0, 0, 20, 10, 18, 5, 3))
print("la chiamata precedente dovrebbe restituire False\n")
print(cerchio_in_rettangolo(0, 0, 20, 10, 15, 2, 3))
print("la chiamata precedente dovrebbe restituire False\n")

