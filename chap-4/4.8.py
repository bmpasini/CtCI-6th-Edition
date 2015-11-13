# Design an algorithm and write code to find the first common ancestor of two nodes in a
# binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

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

# with parent

# with no parent

# Time complextity: O(n)
def first_common_ancestor1(bst, p, q):
    if not in_subtree(bst.root, p) or not in_subtree(bst.root, q):
        return None
    return _first_common_ancestor1(bst.root, p, q)

def _first_common_ancestor1(x, p, q): # pass root in
    if x is None:
        return None
    if x == p or x == q:
        return x
    is_p_on_the_left = in_subtree(x.left, p) # takes 1/2 the number of calls each time
    is_q_on_the_left = in_subtree(x.left, q)
    if is_p_on_the_left != is_q_on_the_left:
        return x
    if is_p_on_the_left:
        return _first_common_ancestor1(x.left, p, q)
    else:
        return _first_common_ancestor1(x.right, p, q)

# Time complextity: O(n)
def in_subtree(x, p):
    if x is None:
        return False
    if x == p:
        return True
    return in_subtree(x.left, p) or in_subtree(x.right, p)

# optimizing it
def first_common_ancestor2(bst, p, q):
    x, is_ancestor = _first_common_ancestor2(bst.root, p, q)
    if is_ancestor:
        return x
    else:
        return None

def _first_common_ancestor2(x, p, q): # pass root in
    if not x:
        return (None, False)

    if x == p and x == q:
        return (x, True)

    v, is_ancestor = _first_common_ancestor2(x.left, p, q)
    if v and v != p and v != q: # pass on ancestor
        return (v, is_ancestor)

    w, is_ancestor = _first_common_ancestor2(x.right, p, q)
    if w and w != p and w != q: # pass on ancestor
        return (w, is_ancestor)

    if v and w: # found common ancestor
        return (x, True)

    elif x == p or x == q:
        return (x, v is not None or w is not None)

    elif v:
        return (v, False)

    elif w:
        return (w, False)

    else:
        return (None, False)


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
    p = bst.root.left.left
    q = bst.root.left.right.left
    print(first_common_ancestor1(bst, p, q).key) # => 4
    print(first_common_ancestor2(bst, p, q).key) # => 4
    p = bst.root.right.right.left
    q = bst.root.right.right.right
    print(first_common_ancestor1(bst, p, q).key) # => 14
    print(first_common_ancestor2(bst, p, q).key) # => 14
    p = bst.root.right.right.left
    q = bst.root.left.right.right
    print(first_common_ancestor1(bst, p, q).key) # => 8
    print(first_common_ancestor2(bst, p, q).key) # => 8
    p = bst.root.left.right.left
    q = bst.root.left.right.right
    print(first_common_ancestor1(bst, p, q).key) # => 6
    print(first_common_ancestor2(bst, p, q).key) # => 6
    p = bst.root.left.left.left
    q = bst.root.left.right.right
    print(first_common_ancestor1(bst, p, q).key) # => 4
    print(first_common_ancestor2(bst, p, q).key) # => 4
