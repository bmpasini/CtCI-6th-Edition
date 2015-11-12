class Node(object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        old_top = self.top
        self.top = old_top.next
        return old_top.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())