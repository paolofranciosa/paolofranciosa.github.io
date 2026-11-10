def cerca(testo, parola): # due sequenze
    '''restituisce la prima posizione di TESTO in cui compare PAROLA,
restituisce -1 se non compare mai'''
    for pos_iniziale in range(len(testo)-len(parola) + 1):
        if esiste_copia(testo, pos_iniziale, parola):
            return pos_iniziale
    return -1

def cerca_ultima(testo, parola): # due sequenze
    '''restituisce l'ultima posizione di TESTO in cui compare PAROLA,
restituisce -1 se non compare mai'''
    for pos_iniziale in range(len(testo)-len(parola), -1, -1):
        if esiste_copia(testo, pos_iniziale, parola):
            return pos_iniziale
    return -1

def esiste_copia(testo, pos_iniziale, parola):
    ''' verificare se la porzione di TESTO da POS_INIZIALE è uguale a PAROLA'''
    for i in range(len(parola)):
        if parola[i] != testo[pos_iniziale+i]:
            return False
    return True

if __name__ == "__main__":
    print(cerca_ultima("torno a casa", "a"))
    print(cerca_ultima("torno a casa", "o"))
    print(cerca_ultima("torno a casa", "rno a c"))
    print(cerca_ultima("torno a casa", "rnx"))
    