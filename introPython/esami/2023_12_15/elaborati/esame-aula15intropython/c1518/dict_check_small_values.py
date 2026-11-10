def dict_check_small_values(d,threshold):
    k=True
    for keys in d:
        if d[keys]>threshold:
            k=False
    return(k)

