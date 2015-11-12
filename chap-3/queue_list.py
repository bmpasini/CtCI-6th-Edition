class Queue(object):

    def __init__(self):
        self.q = list() # insert left, remove right

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.q)

    def enqueue(self, data):
        self.q.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue underflow.")
        else:
            return self.q.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Queue underflow.")
        else:
            return self.q[-1]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())
    q.enqueue(5)
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())