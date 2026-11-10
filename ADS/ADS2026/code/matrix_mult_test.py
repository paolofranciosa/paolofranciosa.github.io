import random

def random_mat_dimensions(n):
    '''generates a list of n pairs, in which each pair contains two integers
in [1,10] and the last element of each pair equals the first element of next pair.
It is used to test optimization code for matrix chain multiplication'''
    dim_min, dim_max = 1, 10
    first = random.randint(dim_min, dim_max)
    res = []
    for i in range(n):
        second = random.randint(dim_min, dim_max)
        res.append([first, second])
        first = second
    return res
    
print(random_mat_dimensions(10))