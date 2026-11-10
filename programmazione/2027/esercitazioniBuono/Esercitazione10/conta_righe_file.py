def conta_righe_file(nomefile):
    if not isinstance(nomefile, str):
        raise TypeError
    num = 0
    with open(nomefile) as f:
        for riga in f:
            num += 1
    return num
