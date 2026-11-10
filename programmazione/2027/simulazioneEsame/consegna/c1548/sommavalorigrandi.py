def sommavalorigrandi(D, soglia):
    ''' La funzione prende in input un dizionario e un valore numerico.
Calcola la somma di tutti i valori corrispondenti ad una chiave del dizionario
che siano maggiori della soglia indicata dal secondo valore. '''


diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,30))
print(sommavalorigrandi(diz,120))



#D = {'Luca':19, 'Federica':19, 'Francesca':20, 'Claudio':25 }
#soglia = 30
#print(sommavalorigrandi(dict, soglia))