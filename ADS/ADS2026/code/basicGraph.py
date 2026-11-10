class UndirectedGraph:
    def __init__(self):   # CONSTRUCTOR: builds an empty undirected graph
        self.__vertices = dict()
#        self._visited = set()
        
    def add_vertex(self, label):
        '''adds a vertex with label, with an empty edge set. If label already exists, do nothing'''
        if label not in self.__vertices:  # if label exists, do nothing
            self.__vertices[label] = dict()  # new vertex, with empty incident edge set
        
    def add_edge(self, vertex1, vertex2, weight=1):
        '''adds an edge from vertex1 to vertex2 and from vertex2 to vertex1,
with weight 1 if not specified.
If vertex1 and/or vertex2 do not exist, they are added to the graph.
If edge already exists, its weight is updated'''
        if vertex1 not in self.__vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.__vertices:
            self.add_vertex(vertex2)
        self.__vertices[vertex1][vertex2] = weight
        self.__vertices[vertex2][vertex1] = weight
    
    def vertex_exists(self, label):
        '''returns True/False if vertex label exists/not_exists'''
        return label in self.__vertices
    
    def edge_exists(self, v1, v2):
        '''returns True/False if edge v1,v2 exists/not_exists'''
        # it should be a key v2 in dictionary with key v1
        if v1 not in self.__vertices:
            return False
        else:
            return v2 in self.__vertices[v1] # key v2 is in the dict representing edges from v1
        
    #    ALTERNATIVE IMPLEMENTATION (lazy evaluation of "and" helps)
    #    return (v1 in self.__vertices) and (v2 in self.__vertices[v1])
        
    def get_num_vertices(self):
        return len(self.__vertices)
    
    def get_num_edges(self):
        m = 0
        for v in self.__vertices:
            m += len(self.__vertices[v])
        return m // 2
    
    def get_vertices(self):
        return list(self.__vertices.keys())
        
    def get_edges(self):
        e = []
        for v1 in self.__vertices:
            for v2 in self.__vertices[v1]:
                if [v2, v1] not in e:
                    e.append([v1, v2])
        return e
        
    def __str__(self):
        res = f"{self.get_num_vertices()} vertices, {self.get_num_edges()} edges\n"
        for v in self.__vertices:
            res += f'{v} adj to {self.__vertices[v]}\n'
        return res
        
if __name__ == "__main__":
    h = UndirectedGraph()
    h.add_edge(1, 2)
    h.add_edge(1, 3)
    h.add_edge(2, 3)
    h.add_edge(2, 4)
    h.add_edge(2, 5)
    h.add_edge(3, 4)
    h.add_edge(3, 5)
    h.add_edge(4, 5)
    print(h)

