# How would you design the data structures for a very large social network like Facebook or
# Linkedin? Describe how you would design an algorithm to show the connection, or path, between
# two people (e.g., Me -> Bob -> Susan -> Jason -> You).

class Server(object):

    machines = dict()
    person_to_machine_id = dict()

    def get_machine_with_id(self, machine_id):
        return self.machines[machine_id]

    def get_machine_id_for_user(self, person_id):
        return self.person_to_machine_id[person_id]

    def get_person_with_id(self, person_id):
        machine_id = self.get_machine_id_for_user(person_id)
        if machine_id is None:
            return None
        machine = self.get_machine_with_id(machine_id)
        if machine is None:
            return None
        return machine.get_person_with_id(person_id)

class Person(object):

    def __init__(self, _id):
        self.id = _id
        self.friends = list()

    def add_friend(_id):
        self.friends.append(_id)

def find_path_bidirectional_BFS(people, source, destination):
    source_data = BFSData(source)
    dest_data = BSFData(destination)
    while not source_data.is_finished() and not dest_data.is_finished():
        collision = search_level(people, source_data, dest_data)
        if collision is not None:
            return merge_paths(source_data, dest_data, collision.id)
        collision = search_level(people, dest_data, source_data)
        if collision is not None:
            return merge_paths(source_data, dest_data, collision.id)
    return None

def merge_paths(self, bfs1, bfs2, connection):
    end1 = bfs1.visited[connection]
    end2 = bfs2.visited[connection]
    path_one = end1.collapse(False)
    path_two = end2.collapse(True)
    path_two.remove_first()
    path_one.add_all(path_two)
    return path_one

def search_level(people, primary, secondary):
    for i in range(len(primary.to_visit)):
        path_node = primary.to_visit.poll()
        person_id = path_node.person.id
        if secondary.visited.get(person_id) is not None:
            return path_node.person
        person = path_node.person
        friends = person.friends
        for friend_id in friends:
            if primary.visited.get(friend_id) is None:
                friend = people[friend_id]
                next = path_node(friend, path_node)
                primary.visited[friend_id] = next
                primary.to_visit.add(next)
    return None

class PathNode(object):

    def __init__(self, p, previous=None):
        self.person = p
        self.previous_node = previous

    def collapse(self, starts_with_root):
        path = LinkedList()
        node = self
        while node is not None:
            if starts_with_root:
                path.add_last(node.person)
            else:
                path.add_first(node.person)
            node = node.previous_node
        return path

class BFSData(object):

    def __init__(self, root):
        self.source_path = PathNode(self.root)
        self.to_visit = Queue()
        self.to_visit.add(self.source_path)
        self.visited = { root.id : self.source_path }

    def is_finished(self):
        return self.to_visit.is_empty()



