
class Vertex():
    def __init__(self, x):
        self.dist = x
        self.visited = False
        self.next = {}

def graphDistances(g, s):
    re = [Vertex(31 * len(g)) for i in range(len(g))]
    
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] != -1:
                re[i].next[j] = g[i][j]
                
    to_visit = s
    re[s].dist = 0
    unvisited = set([i for i in range(len(g))])
    while unvisited:
        re[to_visit].visited = True
        unvisited.remove(to_visit)
        for el in re[to_visit].next:
            if not re[el].visited:
                edge = re[to_visit].next[el]
                re[el].dist = min(re[el].dist, re[to_visit].dist + edge)
        
        cur_shortest = 31 * len(g)
        to_visit = -1
        temp_set = set()
        for v in unvisited:
            dist = re[v].dist
            if dist < cur_shortest:
                cur_shortest = dist
                to_visit = v
                
    return [re[i].dist for i in range(len(re))]
        
        