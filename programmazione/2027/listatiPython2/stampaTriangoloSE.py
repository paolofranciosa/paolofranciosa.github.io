#       *
#      **
#     ***
#    ****
# .....
# *******
#********
def stampa_triangolo_SE(n):
    for riga in range(1, n+1):
        # stampa n-riga spazi
        for pos in range(n-riga):
            print(" ", end="")
        # stampa riga asterischi
        for pos in range(riga):
            print("*", end="")
        print()    

stampa_triangolo_SE(5)