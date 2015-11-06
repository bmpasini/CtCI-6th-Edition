# Given two linked lists, determine if the two lists intersect (by reference)

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = Node(data)

    def get_node_n(self, n):
        x = self.head
        while x and n != 1:
            n -= 1
            x = x.next
        return x

    def append_node(self, node, n):
        x = self.head
        while x.next and n != 1:
            n -= 1
            x = x.next
        x.next = node

def print_ll(ll):
    x = ll.head
    while x:
        print(x.data, "-> ", end="")
        x = x.next
    print(None)

def print_head(h):
    x = h
    while x:
        print(x.data, "-> ", end="")
        x = x.next
    print(None)

def get_tail_and_cnt(h):
    x = h
    i = 0
    while x.next:
        i += 1
        x = x.next
    return (x, i)

def strip_start(h, i):
    while h and i != 0:
        i -= 1
        h = h.next
    return h

def intersect(h1, h2):
    tail1, i1 = get_tail_and_cnt(h1)
    tail2, i2 = get_tail_and_cnt(h2)
    if tail1 != tail2:
        return None
    x1 = h1
    x2 = h2
    if i1 > i2:
        h1 = strip_start(h1,i1-i2)
    elif i1 < i2:
        h2 = strip_start(h2,i2-i1)
    while h1 and h2:
        if h1.next == h2.next:
            return h1.next
        h1 = h1.next
        h2 = h2.next
    return None

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(3)
    ll1.append(1)
    ll1.append(5)
    ll1.append(9)
    ll1.append(7)
    ll1.append(2)
    ll1.append(1)
    print_ll(ll1)
    n = ll1.get_node_n(5)
    print_head(n)
    ll2 = LinkedList()
    ll2.append(4)
    ll2.append(6)
    ll2.append_node(n, 5)
    print_ll(ll2)
    print(intersect(ll1.head,ll2.head))
