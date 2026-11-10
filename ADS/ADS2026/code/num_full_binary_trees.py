import math

def num_FBT(n_leaves):
    '''returns the number of full binary trees with n leaves.
A closed form formula is known, related to Catalan numbers'''
    known = {1: 1}
    return num_FBT_memo(n_leaves, known)

def num_FBT_memo(n_leaves, known):
    if n_leaves not in known:
        tot = 0
        for i in range(1, n_leaves):
            tot += num_FBT_memo(i, known) * num_FBT_memo(n_leaves-i, known)
        known[n_leaves] = tot
    return known[n_leaves]
    
def num_FBT_trivial(n_leaves):
    if n_leaves == 1:
        return 1
    else:
        tot = 0
        for i in range(1, n_leaves):
            tot += num_FBT_trivial(i) * num_FBT_trivial(n_leaves-i)
        return tot

def closed_form(n):
    return math.comb(2*(n-1), n-1)//n

if __name__ == "__main__":
    print("using dynamic programming")
    for n in range(1,100):
        print(f'num_full_binary_trees({n}) = {num_FBT(n)} ({closed_form(n)})')
    print("trivial computation")
    for n in range(1,100):
        print(f'num_full_binary_trees({n}) = {num_FBT_trivial(n)}')

