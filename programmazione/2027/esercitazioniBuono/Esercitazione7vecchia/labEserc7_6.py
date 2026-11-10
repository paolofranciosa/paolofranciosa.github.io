# labEserc7.6.py

def bitonica(sequenza):
    if not isinstance(sequenza, list):
        raise TypeError
    for x in sequenza:
        if not isinstance(x, (int, float)):
            raise TypeError
    i = 0
    while i < len(sequenza)-1  and  sequenza[i] < sequenza[i+1]:
        i += 1
    if i == 0  or  i == len(sequenza)-1:
        return False
    while i < len(sequenza)-1  and  sequenza[i] > sequenza[i+1]:
        i += 1
    if i == len(sequenza)-1:
        return True
    else:
        return False
