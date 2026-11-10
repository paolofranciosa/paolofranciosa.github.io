def scalar_product(v1,v2):
    if not isinstance(v1,list):
        raise TypeError
    if not isinstance(v2,list):
        raise TypeError
    for i in v1:
        if not isinstance(i,int) and not isinstance(i,float):
            raise TypeError
    for i in v2:
        if not isinstance(i,int) and not isinstance(i,float):
            raise TypeError
    if len(v1) != len(v2):
        raise ValueError
    if len (v1)==0:
        raise ValueError
    if len (v2)==0:
        raise ValueError
    s=0
    for i in range(len(v1)):
        p=v1[i]*v2[i]
        s+=p
    return s
print(scalar_product([1,4,3],[5,5,1]))