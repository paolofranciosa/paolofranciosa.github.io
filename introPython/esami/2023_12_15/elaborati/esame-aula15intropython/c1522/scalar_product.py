def scalar_product(a, b):
    product = 0
    scalar = 0
    for i in range(len(a)):
        product = a[i]*b[i]
        scalar = scalar + product
    return scalar



list1 =[2,2,2]
list2 = [1,2,3]

print(scalar_product(list1,list2))