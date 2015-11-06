class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def push(self, data):
        new_head = Node(data, self.head)
        self.head = new_head
        self.size += 1

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return size

        

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next