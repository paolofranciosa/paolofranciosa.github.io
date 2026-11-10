def mat_count_large(m, threshold):
    if not isinstance(m,list):
        raise TypeError
    for i in range(len(m)):
        if not isinstance(m[i],list):
            raise TypeError
    if not isinstance(threshold,(int,float)):
        raise TypeError
    conta=0
    for row in m:
        for values in row:
            if values>threshold:
                conta+=1
    return conta


