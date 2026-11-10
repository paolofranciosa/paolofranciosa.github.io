def dict_check_small_values(d, soglia):
    for k in d:
        if d[k] >= soglia:
            return False
    return True

