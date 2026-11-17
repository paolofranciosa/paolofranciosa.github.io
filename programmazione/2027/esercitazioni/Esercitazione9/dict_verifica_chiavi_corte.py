def dict_verifica_chiavi_corte(d, soglia):
    for k in d:
        if len(k) > soglia:
            return False
    return True

