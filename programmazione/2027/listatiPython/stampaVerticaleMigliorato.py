def stampa_verticale(stringa1, stringa2):
    '''stampa le due stringhe in verticale, separate da due
colonne di spazi'''

    lungh_comune = min(len(stringa1), len(stringa2))
    # stampa in ogni caso la parte iniziale

    for i in range(lungh_comune):
            print(stringa1[i], stringa2[i], sep = "  ")
            
    # stampa la parte residua della prima o della seconda
    if len(stringa1) > len(stringa2):
        for i in range(lungh_comune, len(stringa1)):
            print(stringa1[i])

    else:
        for i in range(lungh_comune, len(stringa2)):
            print("   ", stringa2[i], sep = "")

stampa_verticale("pippo", "pluto")
print()
stampa_verticale("pippo", "topolino")
print()
stampa_verticale("topolino", "pippo")
        
            