from QueueModule import Queue
from StackModule import Stack
from ItalyGraph import *

class UndirectedGraph:
    def __init__(self):
        self._vertices = dict()
        self._visited = set()
        
    def add_vertex(self, label):
        self._vertices[label] = dict()
        
    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self._vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self._vertices:
            self.add_vertex(vertex2)
        self._vertices[vertex1][vertex2] = weight
        self._vertices[vertex2][vertex1] = weight
    
    def get_num_vertices(self):
        return len(self._vertices)
    
    def get_num_edges(self):
        m = 0
        for v in self._vertices:
            m += len(self._vertices[v])
        return m // 2
    
    def get_vertices(self):
        return list(self._vertices.keys())
        
    def get_edges(self):
        e = []
        for v1 in self._vertices:
            for v2 in self._vertices[v1]:
                if [v2, v1] not in e:
                    e.append([v1, v2])
        return e
        
    def bfs_visit(self, radix):
        v_list = [radix]
        queue = Queue()
        visited = set()
        visited.add(radix)
        queue.push(radix)
        while not queue.empty():
            v = queue.pop()
            for p in self._vertices[v]:
                if p not in visited:
                    v_list.append(p)
                    visited.add(p)
                    queue.push(p)
        return v_list
    
    def dfs_visit_rec(self, v):
        self._visited.add(v)
        vertex_list = [v]
        for p in self._vertices[v]:
            if p not in self._visited:
                vertex_list.extend(self.dfs_visit_rec(p))
        return vertex_list
        
    def dfs_visit(self, radix):
        v_list = []
        stack = Stack()
        visited = set()
        stack.push(radix)
        while not stack.empty():
            v = stack.pop()
            if v not in visited:
                v_list.append(v)
                visited.add(v)
                for p in self._vertices[v]:
                    stack.push(p)
        return v_list              
                
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
        parent = dict()
        parent[radix] = None
        while not stack.empty():
            v = stack.pop()
            if v not in visited:
                if parent[v] is not None: # it is False only for radix
                    tree.add_edge(parent[v], v)
                visited.add(v)
                for p in self._vertices[v]:
                    stack.push(p)
                    parent[p] = v
        return tree           
                
    def __str__(self):
        res = f"{self.get_num_vertices()} vertices, {self.get_num_edges()} edges\n"
        for v in self._vertices:
            res += f'{v} adj to {self._vertices[v]}\n'
        return res


class DirectedGraph(UndirectedGraph):
    
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
    
    def get_vertices(self):
        return list(self._vertices.keys())
        

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
print("BFS visit:", h.bfs_visit(1))
print("BFS tree:", h.bfs_tree(1))
print("DFS visit:", h.dfs_visit(1))
print("DFS visit rec:", h.dfs_visit_rec(1))
print("DFS tree:", h.dfs_tree(1))

#i = build_Italy()
#print("DFS visit:", i.dfs_visit("Lazio"))
#print("DFS visit rec:", i.dfs_visit_rec("Lazio"))

