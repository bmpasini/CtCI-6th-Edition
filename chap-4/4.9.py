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

    def remove(self, node):
        if self.head is None:
            return None
        if self.head.data == node:
            self.head = self.head.next
            return node
        prev = None
        x = self.head
        while x:
            if x.data == node:
                prev.next = x.next
                return node
            prev = x
            x = x.next
        return None

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

    def show_bst(self):
        x = self.head
        while x is not None:
            print(x.data.key, end='')
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

    def __iter__(self):
        nodes = list()
        x = self.head
        while x:
            nodes.append(x)
            x = x.next
        return iter(nodes)

def sequences(x):
    result = list()
    if x is None:
        result.append(LinkedList())
        return result
    prefix = LinkedList()
    prefix.add_last(x.key)
    left = sequences(x.left)
    right = sequences(x.right)
    for l in left:
        for r in right:
            weaved = list()
            weave(l, r, prefix, weaved)
            result += weaved
    return result

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

def sequences2(bst):
    all_seqs = list()
    build_seqs(bst.root, list(), list(), all_seqs)
    return all_seqs

def build_seqs(x, building, seq, all_seqs): # building is a queue (append left, remove right)
    seq.append(x.key)
    if x.left:
        building.insert(0, x.left)
    if x.right:
        building.insert(0, x.right)
    if len(building) == 0:
        all_seqs.append(seq)
    for i in range(len(building)):
        x = building.pop()
        build_seqs(x, building.copy(), seq.copy(), all_seqs)
        building.insert(0, x)

if __name__ =="__main__":
    bst = BST()
    bst.put(8)
    bst.put(4)
    bst.put(12)
    bst.put(2)
    bst.put(6)
    bst.put(10)
    # bst.put(14)
    # bst.put(1)
    # bst.put(3)
    # bst.put(5)
    # bst.put(7)
    # bst.put(9)
    # bst.put(11)
    # bst.put(13)
    # bst.put(15)
    for l in sequences(bst.root):
        l.show()
    print("-----")
    for l in sequences2(bst):
        print(l)
    # sequences(bst.root)
    # sequences2(bst)
    # l1 = LinkedList()
    # l1.add_last(1)
    # l1.add_last(2)
    # l1.add_last(3)
    # l1.show()
    # l2 = LinkedList()
    # l2.add_last(4)
    # l2.add_last(5)
    # l2.add_last(6)
    # l2.show()
    # ary = list()
    # weave(l1,l2,LinkedList(),ary)
    # for ll in ary:
    #     ll.show()



