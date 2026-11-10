def dict_reduced(d, threshold):
    new_d = {}
    for k in d:
        if d[k] > threshold:
            new_d[k] = d[k]
    return new_d

