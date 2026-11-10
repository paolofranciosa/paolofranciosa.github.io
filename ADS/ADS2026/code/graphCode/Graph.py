from QueueModule import Queue
from StackModule import Stack
from PriorityQueue import PriorityQueue

class UndirectedGraph:
    def __init__(self):   # CONSTRUCTOR: builds an empty undirected graph
        self._vertices = dict()
        
    def add_vertex(self, label):
        '''adds a vertex with label, with an empty edge set. If label already exists,
does nothing'''
        if label not in self._vertices:  # if label exists, do nothing
            self._vertices[label] = dict()  # new vertex, with empty incident edge set
        
    def add_edge(self, vertex1, vertex2, weight=1):
        '''adds an edge from vertex1 to vertex2, with weight 1 if not specified.
If vertex1 and/or vertex2 do not exist, they are added to the graph.
If edge already exists, its weight is updated'''
        if vertex1 not in self._vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self._vertices:
            self.add_vertex(vertex2)
        self._vertices[vertex1][vertex2] = weight
        self._vertices[vertex2][vertex1] = weight # in an undirected graph each edge is in two adjacency lists
    
    def vertex_exists(self, label):
        '''returns True/False if vertex label exists/not_exists'''
        return label in self._vertices  #  "x in y" is a boolean expression
    
    def edge_exists(self, v1, v2):
        '''returns True/False if edge v1,v2 exists/not_exists'''
        # there should be a key v2 in dictionary with key v1
        if v1 not in self._vertices:
            return False
        else:
            return v2 in self._vertices[v1] # key v2 is in the dict representing edges from v1
        
    #    ALTERNATIVE IMPLEMENTATION (lazy evaluation of "and" makes it correct)
    #    return (v1 in self._vertices) and (v2 in self._vertices[v1])
        
    def get_num_vertices(self):
        '''returns the number of vertices in the graph'''
        return len(self._vertices)
    
    def get_num_edges(self):
        '''returns the number of edges in the graph'''
        m = 0
        for v in self._vertices:
            m += len(self._vertices[v])
        return m // 2
    
    def get_vertices(self):
        '''returns a list of all vertices in the graph'''
        return list(self._vertices.keys())
        
    def get_edges(self):
        '''returns a list of all edges in the graph, each edge (a,b) is returned only one time
        i.e., (b,a) is not returned'''
        e = []
        for v1 in self._vertices:
            for v2 in self._vertices[v1]:
                if v1 < v2:
                    e.append([v1, v2, self._vertices[v1][v2]])
        return e
        
    def bfs_visit(self, radix):
        '''returns vertices in a BFS visit sequence starting from radix'''
        queue = Queue()    # visit must continue from these vertices
                           #       (vertices in queue are already been visited)
        visited = set()    # set of visited vertices (only for improving efficiency)
                           # set is a Python class: hash table containing 
                           #       only keys, with no values
        v_list = [radix]   # list of visited vertices, to be returned
        
        visited.add(radix) 
        queue.push(radix)  # vertices adj to radix have to be visited
        while not queue.empty():
            v = queue.pop()
            for p in self._vertices[v]: # for each neighbor of v
                if p not in visited:
                    v_list.append(p)
                    visited.add(p)
                    queue.push(p)
        return v_list
    
    def dfs_visit(self, radix):
        '''returns vertices in a DFS visit sequence starting from radix'''
        stack = Stack()    # visit must continue from these vertices
                           #      (vertices in stack are possibly to be visited)
        visited = set()    # set of visited vertices (only for improving efficiency)
        v_list = []        # list of visited vertices, to be returned
        
        stack.push(radix)  # vertices adj to radix have to be visited
        while not stack.empty():
            v = stack.pop()
            if v not in visited: # a vertex in the stack could be already visited
                                 #     due to alternative paths
                v_list.append(v)
                visited.add(v)
                for p in self._vertices[v]:
                    stack.push(p)
        return v_list              
                
    def dfs_visit_rec(self, v): # method to be invoked for visiting the graph. Just calls dfs_visit_recursive
        visited = set()  # this variable improves efficiency.
                         # It could be omitted, testing whether a vertex is
                         # in vertex_list, but this test would require linear expected time.
        vertex_list = []
        self.dfs_visit_recursive(v, vertex_list, visited)
        return vertex_list
        
    def dfs_visit_recursive(self, v, vertex_list, visited): # this is the recursive method
        visited.add(v)
        vertex_list.append(v)
        for p in self._vertices[v]:
            if p not in visited:
                self.dfs_visit_recursive(p, vertex_list, visited)
        
    def bfs_tree(self, radix):
        tree = DirectedGraph()
        queue = Queue()
        visited = set()
        visited.add(radix)
        queue.push(radix)
        while not queue.empty():
            v = queue.pop()
            for p in self._vertices[v]:
                if p not in visited:
                    tree.add_edge(v,p)
                    visited.add(p)
                    queue.push(p)
        return tree
        
    def dfs_tree(self, radix):
        tree = DirectedGraph()
        stack = Stack()
        visited = set()
        stack.push(radix)
        parent = dict()  # stores the candidate parent for each vertex in the stack
        parent[radix] = None
        while not stack.empty():
            v = stack.pop()
            if v not in visited:
                if parent[v] is not None: # it is False only for radix
                    tree.add_edge(parent[v], v)
                visited.add(v)
                for p in self._vertices[v]: # look at all neighbors
                    stack.push(p)
                    parent[p] = v
        return tree           
                
    def dfs_tree_rec(self, v): # method to be invoked for building the tree. Just calls dfs_tree_recursive
        visited = set()
        tree = DirectedGraph()
        self.dfs_tree_recursive(v, tree, visited)
        return tree

    def dfs_tree_recursive(self, v, tree, visited): # this is the recursive method
        visited.add(v) # uses a global dict for storing visited vertices
        for p in self._vertices[v]:
            if p not in visited:
                tree.add_edge(v, p)
                self.dfs_tree_recursive(p, tree, visited)
        
    def sssp_tree(self, radix):
        '''implements Dijkstra algorithm'''
        queue = PriorityQueue() # contains pairs  vertex, priority
        distance = dict()       # stores (candidate) distances of vertices from radix
        parent = dict()         # stores the (candidate) parent of each vertex in the SSSP tree
        distance[radix] = 0
        parent[radix] = None
        queue.insert(radix, 0)
        while not queue.is_empty():
            v, v_dist = queue.pop_min()
            for p in self._vertices[v]:
                alt_dist = v_dist + self._vertices[v][p]
                if p not in distance or alt_dist < distance[p]:
                        # modifies candidate parent, distance, and priority in queue
                    parent[p] = v
                    distance[p] = alt_dist
                    queue.insert(p, alt_dist) # inserts a new item in the priority queue,
                                              # or improves its priority if already present 

        tree = DirectedGraph()
        for v in parent: # builds the SSSP tree
            par = parent[v]
            if par is not None:
                tree.add_edge(par, v, self._vertices[par][v])
        return tree
    
    def minimum_spanning_forest_Prim(self):
        '''returns a minimum spanning forest of an undirected graph, implementing Prim's algorithm'''
        forest = UndirectedGraph()
        queue = PriorityQueue() # contains pairs (vertices, priority).
                                # priority of v is the weight of the minimum edge
                                # connecting the current tree to vertex v
        for v in self.get_vertices():  # each vertex has infinite distance from the tree
            queue.insert(v, float("inf")) # float value representing infinite
            forest.add_vertex(v)  # initially, the forest contains only vertices
        adjacent = dict()        # stores the (candidate) vertex leading to a vertex from the tree
        reached_vertices = set()  # stores vertices already in the forest
        while not queue.is_empty():
            v, weight = queue.pop_min()  # gets the closest vertex from current tree
            forest.add_vertex(v)
            if weight < float('inf'):  # v is adjacent to same connected component
                forest.add_edge(adjacent[v], v, weight)  # this is not performed if v starts a new tree
            reached_vertices.add(v)
            for p in self._vertices[v]:  # for each neighbor of v
                if p not in reached_vertices:
                    if p not in adjacent or self._vertices[v][p] < self._vertices[adjacent[p]][p]: # p was not reachable or current edge is better
                        # modifies candidate parent and priority in queue
                        adjacent[p] = v
                        queue.insert(p, self._vertices[v][p]) # inserts a new item in the priority queue,
                                              # or improves its priority if already present 
        return forest
    
    def minimum_spanning_forest_Kruskal(self):
        '''returns a minimum spanning forest of an undirected graph, implementing Kruskal's algorithm'''
        forest = UndirectedGraph()
        # each tree in the forest is represented by one of its vertices
        vertices = dict()  # a dict of sets. Keys are the representative vertices,
                           # each representative vertex is associated to the set
                           # storing all the vertices in that tree
        tree_num = dict()  #  for each vertex, the tree it belongs to (represented by a vertex)
        for v in self.get_vertices():
            forest.add_vertex(v)      # in the initial forest, each vertex is a singleton tree
            tree_num[v] = v           # each vertex is a singleton tree
            vertices[v] = set()
            vertices[v].add(v)
        edge_pq = PriorityQueue() # stores edges, using weight as priority (min on top)
        for e in self.get_edges():
            edge_pq.insert((e[0], e[1]), e[2]) # each element in the priority queue is a pair
                                               # ((x,y), w) made by an edge (x,y) and its weight w
        while not edge_pq.is_empty():
            edge, weight = edge_pq.pop_min()  # gets edges by increasing weight
            v1, v2 = edge
            tree_num1 = tree_num[v1]
            tree_num2 = tree_num[v2]
            if tree_num1 != tree_num2:  # edge v1,v2 joins two different trees
                forest.add_edge(v1, v2, weight)
                if len(vertices[tree_num1]) < len(vertices[tree_num2]):
                    # move vertices from tree_num[v1] to tree_num[v2]
                    largest_tree_num = tree_num2
                    for p in vertices[v1]:
                        vertices[largest_tree_num].add(p)
                        tree_num[p] = largest_tree_num
                else: # move vertices from tree_num[v2] to tree_num[v1]
                    largest_tree_num = tree_num1
                    for p in vertices[v2]:
                        vertices[largest_tree_num].add(p)
                        tree_num[p] = largest_tree_num
        return forest
            
    def __str__(self):
        res = f"{self.get_num_vertices()} vertices, {self.get_num_edges()} edges\n"
        for v in self._vertices:
            res += f'{v} to {self._vertices[v]}\n'
        return res


class DirectedGraph(UndirectedGraph):
# DirectedGraph is a subclass of UndirectedGraph
# the sublass inherits all methods from the superclass
# here we can add new methods
# and re-define some old methods from the superclass
    
    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self._vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self._vertices:
            self.add_vertex(vertex2)
        self._vertices[vertex1][vertex2] = weight

    def get_num_edges(self):
        m = 0
        for v in self._vertices:
            m += len(self._vertices[v])
        return m
    
    def get_edges(self):
        e = []
        for v1 in self._vertices:
            for v2 in self._vertices[v1]:
                e.append([v1, v2])
        return e
        
if __name__ == "__main__":
    h = UndirectedGraph()
    h.add_edge(1, 2, 40)
    h.add_edge(1, 3, 10)
    h.add_edge(2, 3, 20)
    h.add_edge(2, 4, 50)
    h.add_edge(2, 5, 10)
    h.add_edge(3, 4, 5)
    h.add_edge(3, 5, 9)
    h.add_edge(4, 5, 7)
    print("GRAPH: \n", h)
    print("BFS visit:\n", h.bfs_visit(1))
    print("BFS tree:\n", h.bfs_tree(1))
    print("DFS tree:\n", h.dfs_tree(1))
    print("DFS tree rec:\n", h.dfs_tree_rec(1))
    print("DFS visit:\n", h.dfs_visit(1))
    print("DFS visit rec:\n", h.dfs_visit_rec(1))
    print("SSSP tree:\n", h.sssp_tree(1))
    print("minimum spanning forest (Prim):\n", h.minimum_spanning_forest_Prim())
    print("minimum spanning forest (Kruskal):\n", h.minimum_spanning_forest_Kruskal())
    
    g = DirectedGraph()
    g.add_edge("A", "B", 7)
    g.add_edge("B", "A", 23)
    g.add_edge("B", "D", 10)
    g.add_edge("B", "C", 5)
    g.add_edge("C", "D", 3)
    g.add_edge("C", "E", 1)
    g.add_edge("D", "C", 2)
    g.add_edge("D", "G", 3)
    g.add_edge("D", "F", 7)
    g.add_edge("E", "D", 4)
    g.add_edge("G", "F", 6)
    g.add_edge("G", "I", 10)
    g.add_edge("G", "H", 1)
    g.add_edge("H", "I", 2)
    g.add_edge("H", "A", 1)
    print("GRAPH: \n", g)
    print("DFS tree from B:\n", g.dfs_tree("B"))
    print("DFS tree (recursive) from B:\n", g.dfs_tree_rec("B"))
    print("SSSP tree from B:\n", g.sssp_tree("B"))
    
    f = UndirectedGraph()
    f.add_edge('A', 'B', 20)
    f.add_edge('A', 'C', 8)  #
    f.add_edge('B', 'C', 12) #
    f.add_edge('B', 'D', 50) #
    f.add_edge('D', 'E', 3)  #
    f.add_edge('E', 'F', 4)  #
    f.add_edge('E', 'G', 25)
    f.add_edge('F', 'G', 1)  #
    f.add_edge('D', 'G', 6)
    f.add_edge('H', 'I', 4)  #
    f.add_edge('H', 'J', 9)    
    f.add_edge('I', 'J', 6)  #
    f.add_vertex('K')
    print("GRAPH: \n", f)
    print("minimum spanning forest (Prim):\n", f.minimum_spanning_forest_Prim())
    print("minimum spanning forest (Kruskal):\n", f.minimum_spanning_forest_Kruskal())

