def scalar_product(a, b):
    scalpro = 0
    for i in range(len(a)):
        scalpro += a[i] * b[i]
    return scalpro