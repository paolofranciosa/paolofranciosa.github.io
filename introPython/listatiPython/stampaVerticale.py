def stampa_verticale(stringa1, stringa2):
    '''stampa le due stringhe in verticale, separate da due
colonne di spazi'''

    if len(stringa1) == len(stringa2):
        for i in range(len(stringa1)):
            print(stringa1[i], stringa2[i], sep = "  ")
            
    elif len(stringa1) > len(stringa2):
        for i in range(len(stringa2)):
            print(stringa1[i], stringa2[i], sep = "  ")
        for i in range(len(stringa2), len(stringa1)):
            print(stringa1[i])
            
    else:
        for i in range(len(stringa1)):
            print(stringa1[i], stringa2[i], sep = "  ")
        for i in range(len(stringa1), len(stringa2)):
            print("   ", stringa2[i], sep = "")

stampa_verticale("pippo", "pluto")
print()
stampa_verticale("pippo", "topolino")
print()
stampa_verticale("topolino", "pippo")
        
            