class Status(object):

    UNVISITED = 1
    VISITING = 2
    VISITED = 3


class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.adj = dict() # key: vertex, val: weight
        self.status = Status.UNVISITED

    def add_edge(self, v, weight=0):
        self.adj[v] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([ x.id for x in self.adj ])

    def get_edges(self):
        return self.adj.keys()

    def get_id(self):
        return self.id

    def get_weight(self, v):
        try:
            return self.adj[v]
        except KeyError:
            raise Exception('These vertices are not connected.')

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status


class Graph(object):

    def __init__(self, digraph=False):
        self.vertices = dict() # key: id, val: vertex
        self.v = 0
        self.digraph = digraph

    def add_vertex(self, key):
        self.v += 1
        self.vertices[key] = Vertex(key)

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None

    def __contains__(self, v):
        return v in self.vertices

    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_edge(self.vertices[t], weight)
        if not self.digraph:
            self.vertices[t].add_edge(self.vertices[f], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def reset_visits(self):
        for v in iter(self):
            v.set_status(Status.UNVISITED)

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vertices)
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)
    for v in g:
        for w in v.get_edges():
            print("( %s , %s )" % (v.get_id(), w.get_id()))

