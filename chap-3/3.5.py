# Write a program to sort a stack such that the smallest items are on the top.
# You may use at most one additional stack to hold items, but you may not copy
# the elements into any other data structure (such as an array). The stack
# supports the following operations: push, pop, peek, and isEmpty.

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        x = self.head
        while x:
            print(x.data, "-> ", end="")
            x = x.next
        print(None)

    def copy(self):
        s = Stack()
        x = self.head
        while x:
            s.push(x.data)
            x = x.next
        return s

def sort(stack):
    s = stack.copy()
    r = Stack()
    while not s.is_empty():
        tmp = s.pop()
        while not r.is_empty() and tmp > r.peek():
            s.push(r.pop())
        r.push(tmp)
    return r


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(5)
    s.push(1)
    s.push(3)
    r = sort(s)
    s.print_stack()
    r.print_stack()
