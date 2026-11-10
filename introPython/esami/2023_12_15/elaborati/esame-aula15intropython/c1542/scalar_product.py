def scalar_product(a, b):
    scalar_prod = 0
    for i in range(len(a)):
        scalar_prod += a[i]*b[i]
    return scalar_prod 
print(scalar_product([1, 4, 3], [5, 5, 1]))