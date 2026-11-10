def multiplying_order(dims):
    return multiplying_order_rec(dims, 0, len(dims))

def multiplying_order_rec(dims, first, last):
    '''dims is a sequence of pairs of integers representing dimensions of matrices
to be multiplied. It is assumed that the second item in each entry equals the first item
in the next entry, so that row-by-column product is well defined.
The function returns the best multiplying strategy for matrices whose dimensions are in positions
from first (included) to last (not included), together with its cost.
We assume that multiplying  n,k  and  k,m  matrices requires nkm operations.
'''
    if last - first == 1: # only one matrix, 0 cost
        return dims[first], 0
        
    # find the best splitting position. Position i means that we first multiply
    # matrices in [first:i], then matrices in [i:last]
    minimum_split_pos = 0
    minimum_cost = None
    for pos in range(first+1, last):
        left_strategy, left_cost = multiplying_order_rec(dims, first, pos)
        right_strategy, right_cost = multiplying_order_rec(dims, pos, last)
        total_cost = left_cost + right_cost + dims[first][0] * dims[pos][0] * dims[last-1][1]
        if minimum_cost is None or total_cost < minimum_cost:
            minimum_split_pos = pos
            minimum_cost = total_cost
            best_left = left_strategy
            best_right = right_strategy
    return (best_left, best_right), minimum_cost
    
if __name__ == "__main__":
    # in pairs: 77
    # from left to right: 186
    # from right to left: 138
    dimensions = ((30,4), (4,20), (20,30), (30,40), (40,6), (6,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30))
#    dimensions = ((30,4), (4,200), (200,30), (30,400), (400,6))
#    dimensions = ((30,4), (4,20), (20,30), (30,40), (40,6), (6,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), )
#    dimensions = ((30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), )
#    dimensions = ((3,4), (4,2))
    print(multiplying_order(dimensions))
    

        
    
