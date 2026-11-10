def multiplying_order(dims):
    memo = {}
    return multiplying_order_worst_rec(dims, 0, len(dims), memo)

def multiplying_order_worst_rec(dims, first, last, memo):
    '''dims is a sequence of pairs of integers representing dimensions of matrices
to be multiplied. It is assumed that the second item in each entry equals the first item
in the next entry, so that row-by-column product is well defined.
The function returns the worst multiplying strategy for matrices whose dimensions are in positions
from first (included) to last (not included), together with its cost.
We assume that multiplying  n,k  and  k,m  matrices requires nkm operations.
'''
    if (first, last) not in memo:
        if last - first == 1: # only one matrix, 0 cost
            memo[(first, last)] = (dims[first], 0)
#        elif last - first == 2: # only two matrices, there is only one possibility
#            memo[(first, last)] = ((dims[first], dims[last-1]), dims[first][0] * dims[first][1] * dims[last-1])
        
        else:    
            # find the worst splitting position. Position i means that we first multiply
            # matrices in [first:i], then matrices in [i:last]
            maximum_split_pos = 0
            maximum_cost = None
            for pos in range(first+1, last):
                left_strategy, left_cost = multiplying_order_worst_rec(dims, first, pos, memo)
                right_strategy, right_cost = multiplying_order_worst_rec(dims, pos, last, memo)
                total_cost = left_cost + right_cost + dims[first][0] * dims[pos][0] * dims[last-1][1]
                if maximum_cost is None or total_cost > maximum_cost:
                    maximum_split_pos = pos
                    maximum_cost = total_cost
                    worst_left = left_strategy
                    worst_right = right_strategy
            memo[(first, last)] = ((worst_left, worst_right), maximum_cost)
    return memo[(first, last)]
    
if __name__ == "__main__":
    # in pairs: 77
    # from left to right: 186
    # from right to left: 138
#    dimensions = ((6,5),(5,4),(4,3),(3,2),(2,1))
    dimensions = ((30,4), (4,20), (20,30), (30,40), (40,6), (6,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30))
#    dimensions = ((3,4), (4,2))
    print(multiplying_order(dimensions))
    

        
    