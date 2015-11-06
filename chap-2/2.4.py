# Write code to partition a list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. 

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        s = ''
        x = self.head
        while x:
            s = ''.join([s, str(x.data), ' -> '])
            x = x.next
        return s + 'None'

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next is not None:
                x = x.next
            x.next = Node(data)

    # Space: O(1)
    # Time: O(n)
    def partition_inplace(self, val):
        prev = None
        x = self.head
        while x:
            if prev and x.data < val:
                prev.next = x.next
                x.next = self.head
                self.head = x
                x = prev.next
            else:
                prev = x
                x = x.next

def print_ll(node):
    while node:
        print(node.data, "-> ", end='')
        node = node.next
    print(None)

def partition(head, val):
    prev = None
    x = head
    while x:
        if prev and x.data < val:
            prev.next = x.next
            x.next = head
            head = x
            x = prev.next
        else:
            prev = x
            x = x.next
    return head
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    print(ll)
    ll.partition_inplace(5)
    print(ll)
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    print(ll)
    head = partition(ll.head, 5)
    print_ll(head)