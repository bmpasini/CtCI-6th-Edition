class Node(object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue(object):

    first = None
    last = None

    def add(self, data):
        new_node = Node(data)
        if self.last:
            self.last.next = new_node
        self.last = new_node
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            return None
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            return None
        return self.first.data

    def is_empty(self):
        return self.first is None


if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(q.remove())
    print(q.remove())
    print(q.remove())
    q.add(4)
    print(q.remove())
    q.add(5)
    print(q.peek())
    print(q.remove())
    print(q.remove())
    print(q.peek())
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    print(q.peek())
    print(q.remove())
    print(q.remove())
    print(q.remove())
    print(q.peek())
    print(q.remove())
    print(q.remove())
    print(q.remove())