# Implement an algorithm to delete a node in the middle of a
# singly linked list, given only access to that node.

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

    def find_middle_element(self):
        prev1 = None
        p1 = self.head
        p2 = self.head
        try:
            while p2.next:
                prev1 = p1
                p1 = p1.next
                p2 = p2.next.next
        except:
            return None
        return p1

    def deleteNode(self, node):
        if node is None or node.next is None:
            return False
        next = node.next
        node.data = next.data
        node.next = next.next
        next = None
        return True

    def deleteNodeN(self, n):
        i = 1
        x = self.head
        while x and i != n:
            x = x.next
            i += 1
        self.deleteNode(x)


if __name__ == "__main__":
    ll = SingleList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.show()
    ll.deleteNodeN(3)
    ll.show()
    
    
