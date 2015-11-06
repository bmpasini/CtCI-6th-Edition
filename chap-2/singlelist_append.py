class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleList(object):

    head = None
    tail = None

    def show(self):
        x = self.head
        while x is not None:
            print(x.data, end='')
            print(" -> ", end='')
            x = x.next
        print(None)

    def append(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        prev = None
        x = self.head
        while x is not None:
            if x.data == node_value:
                if prev is not None:
                    prev.next = x.next
                else:
                    self.head = x.next
                break
            else:
                prev = x
                x = x.next
        if x.next is None:
            self.tail = x
        if self.head is None:
            self.tail = None

    def is_empty(self):
        return self.head is None


if __name__ == "__main__":
    s = SingleList()
    s.append(31)
    s.append(2)
    s.append(3)
    s.append(4)
    s.show()
    s.remove(31)
    s.remove(3)
    s.remove(2)
    s.show()
    s.remove(4)
    s.show()
    s.append(5)
    s.append(3)
    s.append(31)
    s.append(2)
    s.show()