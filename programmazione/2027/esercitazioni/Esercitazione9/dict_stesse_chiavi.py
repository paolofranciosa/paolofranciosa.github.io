def dict_stesse_chiavi(d1, d2):
    if not isinstance(d1, dict):
        raise TypeError
    if not isinstance(d2, dict):
        raise TypeError
    if len(d1) != len(d2):
        return False
    for k in d1:
        if k not in d2:
            return False
    return True
 

