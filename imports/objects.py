"""

"""


class DisjointSet:
    """
    My Implementation of disjoint set data structure;
    Currently a work in progress.
    """
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = DefaultDict(set)
    
    
    def add_edge(self, u, v):
        """ adds a connection between 2 vertices in the graph """

        self.graph[u].add(v)
        self.graph[v].add(u)
    

    def subnets(self):
        """ returns a list of subnets """
        
        subnets = list()
        seen = set()
        
        for vertex in range(self.vertices):
            if vertex in seen:
                continue
            
            subnet = set()
            current = {vertex}
            
            while current:
                nxt = set()
                
                for node in current:
                    if node in seen:
                        continue
                    
                    seen.add(node)
                    nxt |= self.graph[node]
                
                subnet |= current
                current = nxt
            
            subnets.append(subnet)
        
        return subnets


class UnionFind:
    """ 
    Disjoint Set data structure and related methods
    optimized with path compression and union by rank
    """


    def __init__(self, size):
        """ initialize the graph with root node and rank values """
        self.root = [i for i in range(size)]
        self.rank = [1] * size


    def find(self, x):
        """ find the root node of node x """
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]


    def union(self, x, y):
        """
        connect nodes x and y to the same root
        root nodes have the highest rank of their disjoint set
        """

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


    def connected(self, x, y):
        """ return whether or not nodes x and y are connected """
        return self.find(x) == self.find(y)


class Undirected_Graph_Node:
    """ Undirected Graph Node object """

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class ListNode:
    """ LeetCode's ListNode object """
    
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None
    

    def __repr__(self):
        tmplt = 'ListNode <{}>\n\tval: {}\n\tprev: {}\n\tnext: {}'
        if self.prev and self.next:
            return tmplt.format(hex(id(self)), self.val, hex(id(self.prev)), hex(id(self.next)))
        elif self.prev:
            return tmplt.format(hex(id(self)), self.val, hex(id(self.prev)), None)
        elif self.next:
            return tmplt.format(hex(id(self)), self.val, None, hex(id(self.next)))
        else:
            return tmplt.format(hex(id(self)), self.val, None, None)


class TreeNode:
    """ LeetCode's TreeNode object """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

    def __repr__(self):
        tmplt = 'TreeNode <{}>\n\tval: {}\n\tleft: {}\n\tright: {}'
        if self.left and self.right:
            return tmplt.format(hex(id(self)), self.val, hex(id(self.left)), hex(id(self.right)))
        elif self.left:
            return tmplt.format(hex(id(self)), self.val, hex(id(self.left)), None)
        elif self.right:
            return tmplt.format(hex(id(self)), self.val, None, hex(id(self.right)))
        else:
            return tmplt.format(hex(id(self)), self.val, None, None)
        