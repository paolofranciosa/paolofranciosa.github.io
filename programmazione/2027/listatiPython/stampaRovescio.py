def stampa_rovescio(s):
    p = len(s)-1
    while p >= 0:
        print(s[p], end="")
        p = p - 1
    print()
    
def uguali(s1, s2):
    ''' restituisce True se s1 ed s2 sono stringhe identiche
False altrimenti'''
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    # ora sono a fine ciclo
    return True

def conta_occorrenze(s, c):
    ''' restituisce il numero di caratteri in s che
sono uguali al carattere c'''
    conta_uguali = 0
    for lettera in s:
        if lettera == c:
            conta_uguali += 1
    return conta_uguali

