def multiplying_order(dims):
    known = {}
    # HERE INITIALIZE known BY ASSOCATING COST 0 TO EACH PAIR (i, i+1)
    return multiplying_order_rec(dims, 0, len(dims), known)

def multiplying_order_rec(dims, first, last, known):
    '''dims is a sequence of pairs of integers representing dimensions of matrices
to be multiplied. It is assumed that the second item in each entry equals the first item
in the next entry, so that row-by-column product is well defined.
The function returns the cost of the best multiplying strategy for matrices whose dimensions
are in positions from first (included) to last (not included).
We assume that multiplying  n,k  and  k,m  matrices requires nkm operations.

In "known" dictionary, keys are pairs (i,j), and values are the best strategy cost for multiplying
matrices from i (include) to j (not included)
'''
    if (first, last) not in known:
        # find the best splitting position. Position i means that we first multiply
        # matrices in [first:i], then matrices in [i:last]
        minimum_split_pos = 0
        minimum_cost = None  # used to allow the first update
        for pos in range(first+1, last):
            # recursively compute the best cost for portions [first, pos] and [pos, last]
            # add the cost for multiplying the results
            # eventually update minimum_split_pos and minimum_cost
            ......
        known[(first, last)] = (minimum_cost)
    return known[(first, last)]
    
if __name__ == "__main__":
#    dimensions = ((6,5),(5,4),(4,3),(3,2),(2,1))
    dimensions = ((30,4), (4,20), (20,30), (30,40), (40,6), (6,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30), (30,4), (4,2), (2,10), (10,1), (1,60), (60,30))
    print("the best strategy for dimensions")
    print(dimensions)
    print("should cost 7220")
    # print here your result
    print(multiplying_order(dimensions))
    

        
    