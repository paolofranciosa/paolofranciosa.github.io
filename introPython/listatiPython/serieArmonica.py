import math

def somma_serie_armonica(n):
    '''restituisce la somma dei reciproci dei primi n naturali'''
    somma = 0
    for i in range(n, 0, -1): #somma i contributi a partire da 1/n, ..., 1/3, 1/2, 1/1
        somma += 1/i
    return somma

if __name__ == "__main__":
    lungh = 2
    print(f'      {"n":15s} {"serie":18s} {"logaritmo":18s} {"differenza":18s}')
    while lungh < 1000000000:
        s = somma_serie_armonica(lungh)
        logaritmo = math.log(lungh)
        print(f'{lungh:15,d} {s:19.15f} {logaritmo:19.15f} {(s-logaritmo):19.15f}')
        lungh *= 2