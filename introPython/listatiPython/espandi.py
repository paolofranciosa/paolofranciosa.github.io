def espandi(frase, n_spazi = 1):
    '''frase e' la sequenza di caratteri da stampare
n_spazi e' il numero di spazi da stampare tra un carattere e l'altro'''

    for i in range(len(frase) - 1):  # esclusa ultima posizione
        print(frase[i], end = " "*n_spazi) # stampa caratteri con spazi
        
    # stampa ultimo carattere con ; e a capo
    print(frase[-1], end = ";\n")
    
espandi("vado a scuola", 3)
espandi("vado a scuola")
