def media(lista, soglia):
    '''assumendo che lista sia una sequenza di numeri,
restituisce la media della sequenza maggiori della soglia'''
    conta_sopra_soglia = 0
    somma_sopra_soglia = 0.0
    for x in lista:
        if x > soglia:
            conta_sopra_soglia += 1
            somma_sopra_soglia += x
    if conta_sopra_soglia == 0:
        raise ValueError
    return somma_sopra_soglia / conta_sopra_soglia
   

def varianza(lista, soglia):
    '''assumendo che lista sia una sequenza di numeri,
restituisce la varianza degli elementi della sequenza maggiori della soglia'''
    med = media(lista, soglia)
    conta = 0
    sommaScartiQuad = 0.0
    for x in lista:
        if x > soglia:
            conta += 1
            sommaScartiQuad += (x - med)*(x - med)
    return sommaScartiQuad / conta

print(varianza([1, 2, 3, 4], 3.5))
