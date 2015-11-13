# Write an algorithm to find the 'next'node (i.e., in-order successor) of a given node in
# a binary search tree. You may assume that each node has a link to its parent.

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

def find_next(x):
    if not x:
        return None
    if x.right:
        return left_most_child(x.right)
    prev = x
    x = x.parent
    while x and x.key < prev.key:
        prev = x
        x = x.parent
    return x

def left_most_child(x):
    while x.left:
        x = x.left
    return x
    
if __name__ == "__main__":
    bst = BST()
    bst.put(8)
    bst.put(4)
    bst.put(12)
    bst.put(2)
    bst.put(6)
    bst.put(10)
    bst.put(14)
    bst.put(1)
    bst.put(3)
    bst.put(5)
    bst.put(7)
    bst.put(9)
    bst.put(11)
    bst.put(13)
    bst.put(15)
    x = bst.root.left
    print(find_next(x).key) # => 5
    x = bst.root.left.right
    print(find_next(x).key) # => 7
    x = bst.root.left.right.right
    print(find_next(x).key) # => 8
    x = bst.root.right.right.left
    print(find_next(x).key) # => 14
    x = bst.root.left.left.left
    print(find_next(x).key) # => 2
    x = bst.root.left.left
    print(find_next(x).key) # => 3
    x = bst.root.left.right.left
    print(find_next(x).key) # => 6
    x = bst.root
    print(find_next(x).key) # => 9
    x = bst.root.right
    print(find_next(x).key) # => 13
    x = bst.root.right.left.right
    print(find_next(x).key) # => 12
    x = bst.root.right.right
    print(find_next(x).key) # => 15
    x = bst.root.right.right.right
    print(find_next(x)) # => None

