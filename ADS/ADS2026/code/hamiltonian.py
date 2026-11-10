def hamiltonian(g, starting_node = None, cycle = False):
    '''given a directed graph g represented by a dict of adjacency lists,
return a list of nodes that constitute a Hamiltonian
path in g. Returns None if g is not Hamiltonian.
starting_node, if specified, is the starting node
cycle specifies whether a hamiltonian cycle instead of a path must be computed
TO BE COMPLETED:
- IMPLEMENT cycle SEARCH,
- choose any starting vertex if path is searched with None starting_node'''
    n = len(g)
    curr_out = {x: 0     for x in g} # position of outgoing edge to be explored
    visited  = {x: False for x in g} # True if x in current path
    path = [None] * (n + 1) # current path, pre-allocated to improve efficiency
    path_len = 0      # used portion of path, from 0 (included) to path_len (excluded)
    
    if starting_node is None:
        path[0] = list(g.keys())[0] # path starts from a random vertex
    else:
        path[0] = starting_node
    visited[path[path_len]] = True
    path_len += 1
    print(f"path {[path[i] for i in range(path_len)]}")
    while path_len < n or (cycle and path_len == n and path[0] != path[-1]):
        head = path[path_len - 1] # last vertex in current path
        next_unvisited_position(head, g, curr_out, visited)
        curr_adj_pos = curr_out[head]
        if curr_adj_pos < len(g[head]):
            next_node = g[head][curr_adj_pos]
            visited[next_node] = True
            path[path_len] = next_node
            path_len += 1
        else:
            curr_out[head] = 0
            visited[head] = False
            path_len -= 1
            if path_len == 0:
                return False
            curr_out[path[path_len - 1]] += 1
        print(f"path {[path[i] for i in range(path_len)]}")
    return path
    
def next_unvisited_position(head, g, curr_out, visited):
    '''increases curr_out[head] looking for an unvisited neighbor.
Set to len(g[head]) if it does not exist'''
    while curr_out[head] < len(g[head]):
        if not visited[g[head][curr_out[head]]]:
            return
        else:
            curr_out[head] += 1
        
# g = {"a": ["b", "c"], "b": ["c", "d"], "c": ["a"], "d": ["c"]}
g1 = {"12": ["23", "21"], "32": ["23", "21"], "23": ["31", "32"], "13": ["31", "32"], "21": ["12", "13"], "31": ["12", "13"]}
print(hamiltonian(g1))
g2 = {"a": ["b", "d"], "b": ["a", "d", "e"], "c": ["f"], "d": ["a", "b", "e", "f"], "e": ["b", "d"], "f": ["d", "c"]}
print(hamiltonian(g2, cycle = True))
g3 = {"a": ["b", "d"], "b": ["a", "d", "e"], "d": ["a", "b", "e"], "e": ["b", "d"]}
print(hamiltonian(g3, cycle = True))
