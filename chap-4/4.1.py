# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

from graph import Graph
from graph import Vertex
from graph import Status

class Queue:

    q = list()

    def enqueue(self, a):
        self.q.insert(0, a)

    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop()

    def __len__(self):
        return len(self.q)

def is_there_a_route(g, v, w):
    if v == w:
        return True
    for x in g:
        x.status = Status.UNVISITED
    q = Queue()
    v.status = Status.VISITING
    q.enqueue(v)
    while len(q) > 0:
        x = q.dequeue()
        for adj_vertex in x.adj:
            if adj_vertex.status == Status.UNVISITED:
                if adj_vertex == w:
                    return True
                adj_vertex.status = Status.VISITING
                q.enqueue(adj_vertex)
        x.status = Status.VISITED
    return False

def is_connected_bfs(g, v, w):
    queue = [ v ] # add left, remove right
    while len(queue) != 0:
        x = queue.pop()
        if x == w:
            return True
        for adj in x.get_edges():
            queue.insert(0, adj)
    return False

def is_connected_dfs(g, v, w):
    connected = list()
    g.reset_visits()
    _is_connected_dfs(g, v, connected)
    return w in connected

def _is_connected_dfs(g, x, connected):
    if x.get_status() == Status.UNVISITED:
        x.set_status(Status.VISITED)
        connected.append(x)
        for adj in x.get_edges():
            _is_connected_dfs(g, adj, connected)

if __name__ == "__main__":
    dg = Graph(True)
    for i in range(6):
        dg.add_vertex(i)
    dg.add_edge(0,1)
    dg.add_edge(0,5)
    dg.add_edge(1,2)
    dg.add_edge(2,3)
    dg.add_edge(3,4)
    dg.add_edge(3,5)
    dg.add_edge(4,0) # add edge and 4 can reach any vertex, disconnect it and 4 cannot reach any
    dg.add_edge(5,4)
    dg.add_edge(5,2)
    for v in dg:
        for w in v.get_edges():
            print("%s -> %s" % (v.get_id(), w.get_id()))
    print("BFS:")
    v = dg.get_vertex(0)
    w = dg.get_vertex(4)
    print(is_connected_bfs(dg, v, w))
    v = dg.get_vertex(4)
    w = dg.get_vertex(0)
    print(is_connected_bfs(dg, v, w))
    w = dg.get_vertex(1)
    print(is_connected_bfs(dg, v, w))
    w = dg.get_vertex(2)
    print(is_connected_bfs(dg, v, w))
    w = dg.get_vertex(3)
    print(is_connected_bfs(dg, v, w))
    w = dg.get_vertex(5)
    print(is_connected_bfs(dg, v, w))
    print("DFS:")
    v = dg.get_vertex(0)
    w = dg.get_vertex(4)
    print(is_connected_dfs(dg, v, w))
    v = dg.get_vertex(4)
    w = dg.get_vertex(0)
    print(is_connected_dfs(dg, v, w))
    w = dg.get_vertex(1)
    print(is_connected_dfs(dg, v, w))
    w = dg.get_vertex(2)
    print(is_connected_dfs(dg, v, w))
    w = dg.get_vertex(3)
    print(is_connected_dfs(dg, v, w))
    w = dg.get_vertex(5)
    print(is_connected_dfs(dg, v, w))
    print("Efficient BFS:")
    v = dg.get_vertex(0)
    w = dg.get_vertex(4)
    print(is_there_a_route(dg, v, w))
    v = dg.get_vertex(4)
    w = dg.get_vertex(0)
    print(is_there_a_route(dg, v, w))
    w = dg.get_vertex(1)
    print(is_there_a_route(dg, v, w))
    w = dg.get_vertex(2)
    print(is_there_a_route(dg, v, w))
    w = dg.get_vertex(3)
    print(is_there_a_route(dg, v, w))
    w = dg.get_vertex(5)
    print(is_there_a_route(dg, v, w))

