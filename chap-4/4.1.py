# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

from graph import Graph
from graph import Vertex

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
    if not x.get_visited():
        x.set_visited(True)
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
    # dg.add_edge(4,0) # add edge and 4 can reach any vertex, disconnect it and 4 cannot reach any
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
