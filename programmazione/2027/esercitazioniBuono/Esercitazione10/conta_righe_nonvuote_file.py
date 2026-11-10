def conta_righe_nonvuote_file(nomefile):
    if not isinstance(nomefile, str):
        raise TypeError
    num = 0
    with open(nomefile) as f:
        for riga in f:
            if len(riga.strip()) > 0:
                num += 1
    return num
