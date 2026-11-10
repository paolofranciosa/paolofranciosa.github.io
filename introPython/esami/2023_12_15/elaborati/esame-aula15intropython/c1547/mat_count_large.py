def mat_count_large(m, threshold):
    if not isinstance(m,list):
        raise TypeError
    for i in m:
        if not isinstance(i,list):
            raise TypeError
    r=len(m)
    c=len(m[0])
    lar=[]
    for i in range(r):
        for j in range(c):
            if m[i][j]>threshold:
                lar.append(m[i][j])
    return len(lar)

