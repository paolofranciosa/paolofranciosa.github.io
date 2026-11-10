def remove_max_frequent_element(a):
    if len(a) == 0:
        return None
    max_f = 0
    for elemento in a:
        f = a.count(elemento)
        if f > max_f:
            ele_m = elemento
            max_f = f
            
    while ele_m in a:
        a.remove(ele_m)
