def dict_check_short_keys(d, soglia):
    for k in d:
        if len(k) > soglia:
            return False
    return True

