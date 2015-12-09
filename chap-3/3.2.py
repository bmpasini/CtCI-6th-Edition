# Design a stack that has O(1) push, pop and min functions

class NodeWithMin(object):

    def __init__(self, data, min_so_far=None, next=None):
        self.data = data
        self.min_so_far = min_so_far
        self.next = next


class StackWithMin(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        if self.head is None or data < self.head.min_so_far:
            self.head = NodeWithMin(data, data, self.head)
        else:
            self.head = NodeWithMin(data, self.head.min_so_far, self.head)

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty.")
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def min(self):
        if self.head is None:
            raise Exception("Stack is empty.")
        else:
            return self.head.min_so_far

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

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            return self.head.data

class StackWithMin2(object):

    min_stack = Stack()
    data_stack = Stack()

    def push(self, data):
        if self.min_stack.is_empty() or data <= self.min_stack.peek():
            self.min_stack.push(data)
        self.data_stack.push(data)        

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            data = self.data_stack.pop()
            if self.min_stack.peek() == data:
                self.min_stack.pop()
            return data

    def min(self):
        return self.min_stack.peek()

    def peek(self):
        return self.data_stack.peek()

    def is_empty(self):
        return self.min_stack.is_empty()


if __name__ == "__main__":
    s = StackWithMin()
    s.push(5)
    s.push(5)
    s.push(3)
    s.push(5)
    s.push(7)
    s.push(1)
    s.push(2)
    s.push(1)
    s.push(7)
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop())
    s = StackWithMin2()
    s.push(5)
    s.push(5)
    s.push(3)
    s.push(5)
    s.push(7)
    s.push(1)
    s.push(2)
    s.push(1)
    s.push(7)
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop(), s.min())
    print(s.pop())
    print(s.min())


# Removing the min element solution in O(k) time, where k is the number of elements before the minumum
# element in the stack

class Node(object):

    def __init__(self, data, _min=None, next=None):
        self.data = data
        self.min = _min
        self.next = next


class Stack(object):

    head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data, data)
        else:
            self.head = Node(data, min(data, self.head.min), self.head)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        data = self.head.data
        self.head = self.head.next
        return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        return self.head.data

    def min(self):
        if self.head is None:
            raise Exception("Stack underflow.")
        if self.head.next is None:
            return self.pop()
        x = self.head
        y = None
        new_min = x.data
        while x.data != x.min:
            new_min = min(new_min, x.data)
            y = Node(x.data, new_min, y)
            x = x.next
        _min = x.data
        if x.next:
            x = x.next
            new_min = x.min
        while y is not None:
            x = Node(y.data, new_min, x)
            y = y.next
        self.head = x
        return _min


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(2)
    s.push(7)
    s.push(1)
    s.push(10)
    s.push(0)
    print(s.min()) # 0
    print(s.min()) # 1
    print(s.min()) # 2
    print(s.pop()) # 10
    print(s.min()) # 3
    print(s.min()) # 5
    print(s.pop()) # 7

