def dict_da_liste(k_list, v_list):

    res = {}
    for i in range(len(k_list)):
        key = k_list[i]
        value = v_list[i]
        res[key] = value
    return res

