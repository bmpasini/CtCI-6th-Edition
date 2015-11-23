# You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects where the first project depends on the second). Find a valid build order. If there is
# none, return an error.

# Digraph --> vertex: project, edge: dependency 
# Topological sort, if there is a cycle return an error
# Topological sort: DFS with a Stack
# Find a cycle: runner method

class State(object):

    UNVISITED = 0
    VISITING = 1
    VISITED = 2

class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.adj = dict() # key: vertex, val: weight
        self.state = State.UNVISITED

    def add_edge(self, v, weight=0):
        self.adj[v] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([ x.id for x in self.adj ])

    def get_edges(self):
        return self.adj.keys()

    def get_id(self):
        return self.id

    def get_weight(self, x):
        return self.adj[x]

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


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
        self.vertices[f].add_edge(self.vertices[t])
        if not self.digraph:
            self.vertices[t].add_edge(self.vertices[f])

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def reset_states(self):
        for v in iter(self):
            v.set_state(State.UNVISITED)

def build_order(g):
    s = [] # add: [].insert(0, el), remove: [].pop(0)
    for v in iter(g):
        if not dfs(s, v):
            return None
    return s

def dfs(s, v):
    if v.get_state() == State.VISITING:
        return False
    if v.get_state() == State.UNVISITED:
        v.set_state(State.VISITING)
        for adj in v.get_edges():
            if not dfs(s, adj):
                return False
        v.set_state(State.VISITED)
        s.insert(0, v.get_id())
    return True

def build_graph(projects, dependencies):
    g = Graph(True)
    for p in projects:
        g.add_vertex(p)
    for t, f in dependencies:
        g.add_edge(f, t)
    return g

if __name__ == "__main__":
    projects = [ "a", "b", "c", "d", "e", "f" ]
    dependencies = [ ("d", "a"), ("b", "f"), ("d", "b"), ("a", "f"), ("c", "d") ]
    g = build_graph(projects, dependencies)
    print(build_order(g))









