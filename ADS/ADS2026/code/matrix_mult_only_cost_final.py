def multiplying_order(dims):
    memo = {}
    return multiplying_order_rec(dims, 0, len(dims), memo)

def multiplying_order_rec(dims, first, last, memo):
    '''dims is a sequence of pairs of integers representing dimensions of matrices
to be multiplied. It is assumed that the second item in each entry equals the first item
in the next entry, so that row-by-column product is well defined.
The function returns the best multiplying strategy for matrices whose dimensions are in positions
from first (included) to last (not included), together with its cost.
We assume that multiplying  n,k  and  k,m  matrices requires nkm operations.
'''
    if (first, last) not in memo:
        if last - first == 1: # only one matrix, 0 cost
            memo[(first, last)] = (0)
        
        else:    
            # find the best splitting position. Position i means that we first multiply
            # matrices in [first:i], then matrices in [i:last]
            minimum_split_pos = 0
            minimum_cost = None
            for pos in range(first+1, last):
                left_cost = multiplying_order_rec(dims, first, pos, memo)
                right_cost = multiplying_order_rec(dims, pos, last, memo)
                total_cost = left_cost + right_cost + dims[first][0] * dims[pos][0] * dims[last-1][1]
                if minimum_cost is None or total_cost < minimum_cost:
                    minimum_split_pos = pos
                    minimum_cost = total_cost
            memo[(first, last)] = (minimum_cost)
    return memo[(first, last)]
    
if __name__ == "__main__":
#    dimensions = ((6,5),(5,4),(4,3),(3,2),(2,1))
    dimensions = ((30,4), (4,20), (20,30), (30,40), (40,6), (6,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30))
    print(multiplying_order(dimensions))
    

        
    