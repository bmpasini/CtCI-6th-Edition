class Stack(object):

    def __init__(self):
        self.q = list() # insert right, remove right

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.q)

    def push(self, data):
        self.q.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        else:
            return self.q.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        else:
            return self.q[-1]

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