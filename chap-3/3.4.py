# Implement a MyQueue class which implements a queue using two stacks.

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


class MyQueue(object):

    def __init__(self):
        self.enqueue_order = Stack()
        self.dequeue_order = Stack()
        self.is_in_enqueued_order = True
        
    def enqueue(self, data):
        if not self.is_in_enqueued_order:
            while not self.dequeue_order.is_empty():
                self.enqueue_order.push(self.dequeue_order.pop())
        self.is_in_enqueued_order = True
        self.enqueue_order.push(data)

    def dequeue(self):
        if self.is_in_enqueued_order:
            while not self.enqueue_order.is_empty():
                self.dequeue_order.push(self.enqueue_order.pop())
        self.is_in_enqueued_order = False
        if self.dequeue_order.is_empty():
            raise Exception("Queue is empty.")
        return self.dequeue_order.pop()

    def peek(self):
        if self.is_in_enqueued_order:
            while not self.enqueue_order.is_empty():
                self.dequeue_order.push(self.enqueue_order.pop())
        self.is_in_enqueued_order = False
        if self.dequeue_order.is_empty():
            raise Exception("Queue is empty.")
        return self.dequeue_order.peek()

    def is_empty(self):
        return self.enqueue_order.is_empty() and self.dequeue_order.is_empty()


if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())


