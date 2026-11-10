from itertools import combinations
import random
import time

def subset_sum_brute_force(value_list, total, epsilon = 0):
    '''given a list of integers value_list, returns a list of lists in which each list 
    contains a subset of value_list whose sum differs from total 
    by at most epsilon'''
    result = []
    for dim in range(len(value_list) + 1):
        for subset in combinations(value_list, dim):
            if abs(sum(subset) - total) <= epsilon:
                result.append(list(subset))
    return result
   
def compute_min_max_sums(value_list):
    minimum_sum = [0] * len(value_list) # in position p there is the minimum sum of elements in value_list[p:]
    maximum_sum = [0] * len(value_list) # in position p there is the maximum sum of elements in value_list[p:]
    if value_list[-1] > 0:
        minimum_sum[-1] = 0
        maximum_sum[-1] = value_list[-1]
    if value_list[-1] < 0:
        minimum_sum[-1] = value_list[-1]
        maximum_sum[-1] = 0
    for p in range(len(value_list)-2, -1, -1):
        if value_list[p] >= 0:
            minimum_sum[p] = minimum_sum[p+1]
            maximum_sum[p] = maximum_sum[p+1] + value_list[p]
        if value_list[p] < 0:
            minimum_sum[p] = minimum_sum[p+1] + value_list[p]
            maximum_sum[p] = maximum_sum[p+1]
    return minimum_sum, maximum_sum
 
def subset_sum(value_list, total, epsilon = 0):
    minimum_sum, maximum_sum = compute_min_max_sums(value_list)
    results = []
    subset_sum_recursive(value_list, total, epsilon, results, [], minimum_sum, maximum_sum, 0)
    return results
    
def subset_sum_recursive(value_list, total, epsilon, result, current_set, minimum_sum, maximum_sum, pos):
    current_sum = sum(current_set)
    # base case: all items in value_list have been considered
    if pos == len(value_list):
        # the end of the list has been reached: we could have a result!
        if total - epsilon <= current_sum and current_sum <= total + epsilon:
            result.append(current_set)
        return
    # base case: the minimum sum of remaining items is to large to to stay in total + epsilon 
    if current_sum + minimum_sum[pos] > total + epsilon:
        return
    # base case: the maximum sum of remaining items is not sufficient to reach total - epsilon 
    if current_sum + maximum_sum[pos] < total - epsilon:
        return

    # recursive step
    current_set_without_pos = current_set.copy()
    subset_sum_recursive(value_list, total, epsilon, result, current_set_without_pos, minimum_sum, maximum_sum, pos+1)
    current_set_with_pos = current_set + [value_list[pos]]
    subset_sum_recursive(value_list, total, epsilon, result, current_set_with_pos, minimum_sum, maximum_sum, pos+1)

if __name__ == "__main__":
    n = 28
    v = [random.randint(-10, 10) for i in range(n)]
    tot = 2*n
    print("heuristic")
    start = time.time()
    r = subset_sum(v, tot)
    rec_duration = time.time()-start
#    print(r)
    len_rec = len(r)
    print(f'found {len_rec} solutions by pruned recursion in {rec_duration:.8f} seconds')

    print("brute force")
    start = time.time()
    r = subset_sum_brute_force(v, tot)
    brute_duration = time.time()-start
#    print(r)
    len_brute = len(r)   
    print(f'found {len_brute} solutions by brute force in {brute_duration:.8f} seconds')

