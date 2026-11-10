def scalar_product(a,b):
    j = 0
    r = 0
    for i in a:
        r += i * b[j]
        j += 1
    return r
