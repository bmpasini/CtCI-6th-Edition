class Node(object):

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList(object):
    
    head = None
    tail = None

    def add_head(self, data):
        new_node = Node(data, next=self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

    def add_tail(self, data):
        new_node = Node(data,prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

    def remove_head(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        if self.head == self.tail:
            self.tail = None
        return data

    def remove_tail(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        if self.head == self.tail:
            self.head = None

    def show(self):
        x = self.head
        print("None <-> ", end="")
        while x:
            print(x.data, "<-> ", end="")
            x = x.next
        print(None)


if __name__ == "__main__":
    l = DoublyLinkedList()
    l.add_head(3)
    l.add_head(2)
    l.add_head(1)
    l.show()
    l.add_tail(4)
    l.add_tail(5)
    l.add_tail(6)
    l.show()
    l.remove_tail()
    l.remove_head()
    l.show()
    l.remove_tail()
    l.remove_head()
    l.show()
    l.remove_tail()
    l.remove_head()
    l.show()
    l.add_head(3)
    l.add_head(2)
    l.add_head(1)
    l.show()
    l.add_tail(4)
    l.add_tail(5)
    l.add_tail(6)
    l.show()
    l.remove_tail()
    l.remove_head()
    l.show()
    l.remove_tail()
    l.remove_head()
    l.show()
    l.remove_tail()
    l.remove_head()
    l.show()