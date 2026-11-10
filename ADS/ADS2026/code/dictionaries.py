import random
import time

def random_list_even_values(min_val, max_val, dim):
    '''returns a list with length dim containing (possibly repeated) even numbers in
[2*min_val, 2*max_val]'''
    s = [0] * dim
    for i in range(dim):
        s[i] = random.randint(min_val, max_val) * 2
    return s

def random_dict_even_values(min_val, max_val, dim):
    '''returns a dict with length dim (approximately) containing even numbers (keys) in
[min_val, max_val]. Each key is associated a same value "aa" '''
    d = {}
    for i in range(dim):
        k = random.randint(min_val, max_val)
        d[k] = "aa"
    return d

def perform_many_searches(structure, num):
    '''performs num searches of an odd number in structure.
Returns elapsed time in seconds'''
    start = time.time()
    look = 567
    for i in range(num):
        if look in structure:
            return 555 # this will never happen
    end = time.time()
    return end - start

def binary_search(s, x):
    start = 0
    end = len(s) - 1
    while start <= end:
        mid = (start + end) // 2
        if s[mid] == x:
            return True
        elif s[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return False

def perform_many_binary_searches(sorted_list, num):
    '''performs num binary searches of an odd number in sorted_list (assumed to be sorted).
Returns elapsed time in seconds'''
    start = time.time()
    look = 567
    for i in range(num):
        if binary_search(sorted_list, look):
            return 555 # this will never happen
    end = time.time()
    return end - start

num_searches = 10000
print(num_searches, "search operations")
for dim in (200, 800, 3200, 12800, 51200, 204800, 819200, 3276800):
    d = random_dict_even_values(1, 50000000, dim)
    l = random_list_even_values(1, 50000000, dim)
    sorted_l = sorted(l)
    print("dim", dim)
    print("   dict:", perform_many_searches(d, num_searches), "seconds")
    print("   sorted list:", perform_many_binary_searches(sorted_l, num_searches), "seconds")
    print("   list:", perform_many_searches(l, num_searches), "seconds")
