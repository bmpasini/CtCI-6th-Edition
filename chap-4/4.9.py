# A bst was created by traversing through an array from left to right and inserting each element.
# Given a bst with distinct elements, print all possible arrays that could have led to this tree.

class NodeBST(object):

    def __init__(self, key, val=None, parent=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None


class BST(object):

    root = None

    def put(self, key, val=None):    
        self.root = self._put(self.root, key, val, None)
        

    def _put(self, x, key, val, parent):
        if x is None:
            return NodeBST(key, val, parent)
        if key < x.key:
            x.left = self._put(x.left, key, val, x)
        elif key > x.key:
            x.right = self._put(x.right, key, val, x)
        else:
            x.val = val
        return x

    def get(self, key):
        x = self._get(self.root, key)
        if x is None:
            return None
        else:
            return x.val

    def _get(self, x, key):
        if x is None:
            return None
        if key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x

class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    head = None

    def add_first(self, data):
        self.head = Node(data, self.head)

    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = Node(data)

    def remove_first(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_last(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        else:
            prev = None
            x = self.head
            while x.next:
                prev = x
                x = x.next
            prev.next = None
            return x.data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def show(self):
        x = self.head
        while x is not None:
            print(x.data, end='')
            print(" -> ", end='')
            x = x.next
        print(None)

    def clone(self):
        new = LinkedList()
        x = self.head
        while x:
            new.add_last(x.data)
            x = x.next
        return new

    def add_all(self, ll):
        tail = ll.clone()
        if self.head is None:
            return tail
        x = self.head
        while x.next:
            x = x.next
        x.next = tail.head

def ary_to_ll(ary):
    ll = LinkedList()
    for i in ary:
        ll.add_last(i)
    return ll

def ll_to_ary(ll):
    l = ll.clone()
    ary = list()
    while not l.is_empty():
        ary.append(l.remove_last())
    return ary

def sequences(bst):
    ary = list()
    _sequences(x.root, ary)
    return ary

def _sequences(x, ary):
    if x is None:
        return None
    left = _sequences(x.left, ary)
    right = _sequences(x.right, ary)

    # if left is not None and right is not None:
        
    # weave

def weave(l1, l2, prefix, ary):
    if l1.is_empty() or l2.is_empty():
        result = prefix.clone()
        result.add_all(l1)
        result.add_all(l2)
        ary.append(result)
        return None

    h1 = l1.remove_first()
    prefix.add_last(h1)
    weave(l1, l2, prefix, ary)
    prefix.remove_last()
    l1.add_first(h1)

    h2 = l2.remove_first()
    prefix.add_last(h2)
    weave(l1, l2, prefix, ary)
    prefix.remove_last()
    l2.add_first(h2)

        

if __name__ =="__main__":
    # print(sequences(bst))
    l1 = LinkedList()
    l1.add_last(1)
    l1.add_last(2)
    l1.add_last(3)
    l1.show()
    l2 = LinkedList()
    l2.add_last(4)
    l2.add_last(5)
    l2.add_last(6)
    l2.show()
    l = ary_to_ll([1,2,3])
    l.show()
    
    # ary = list()
    # weave(l1,l2,LinkedList(),ary)
    # for ll in ary:
    #     ll.show()




