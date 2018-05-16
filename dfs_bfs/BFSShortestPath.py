class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False
        self.dist = -1
        self.conn = []

class Graph:
    def __init__(self, num):
        self.nodes = [Node(i) for i in range(num)]
        
    def connect(self, i, j):
        self.nodes[i].conn.append(self.nodes[j])
        self.nodes[j].conn.append(self.nodes[i])
        
    def find_all_distances(self, s):
        source = self.nodes[s]
        source.dist = 0
        source.visited = True
        nodes = [source]
        while len(nodes) > 0:
            temp = []
            for root in nodes:
                for node in root.conn:
                    if not node.visited:
                        node.dist = root.dist + 6
                        node.visited = True
                        temp.append(node)
            nodes = temp
                    
        re = ""
        for i in range(len(self.nodes)):
            if i != s:
                re += str(self.nodes[i].dist) + " "
        print re

t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    graph.find_all_distances(s-1)
    