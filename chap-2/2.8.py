# Given a circular linked list,implement an algorithm
# which returns the node at the beginning of the loop.

import time

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

    def short_circuit(self):
        x = self.head
        while x.next:
            x = x.next
        x.next = self.head

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
    head = ll.head
    while head:
        print(head.data, "-> ", end="")
        time.sleep(1)
        head = head.next
    print(None)

def print_head(h):
    x = h
    while x:
        print(x.data, "-> ", end="")
        x = x.next
    print(None)

# space: O(n)
# time: O(n) (if the cycle is broken)
def find_start_of_cycle(h):
    slow = h
    fast = h
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None
    fast = h
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(3)
    ll1.append(1)
    ll1.append(5)
    ll1.append(9)
    ll1.append(7)
    ll1.append(2)
    ll1.append(1)
    ll1.append(0)
    # print_ll(ll1)
    ll1.short_circuit()
    n = ll1.get_node_n(1)
    ll2 = LinkedList()
    ll2.append(4)
    ll2.append(8)
    ll2.append(7)
    ll2.append(2)
    ll2.append_node(n, 4)
    # print_ll(ll2)
    print(find_start_of_cycle(ll2.head).data)

    