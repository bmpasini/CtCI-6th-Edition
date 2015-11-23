# T1 and T2 are very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree
# of n is identical to T2. That is, if you cut off the tree at node n, the two trees
# would be identical.


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

def check_subtree(t1, t2):
    if t1 is None or t2 is None:
        return False
    elif t2.root is None:
        return True # an empty tree is always a subtree
    else:
        return _check_subtree(t1.root, t2.root)

def _check_subtree(x1, r2):
    if x1 is None:
        return False
    if x1.key == r2.key and x1.val == r2.val:
        return check_equal(x1, r2)
    else:
        return _check_subtree(x1.left, r2) or _check_subtree(x1.right, r2)

def check_equal(x1, x2):
    if x1 is None and x2 is None:
        return True
    elif x1 is None or x2 is None:
        return False
    elif x1.key == x2.key and x1.val == x2.val:
        return check_equal(x1.left, x2.left) and check_equal(x1.right, x2.right)
    else:
        return False


if __name__ =="__main__":
    bst1 = BST()
    bst1.put(8)
    bst1.put(4)
    bst1.put(12)
    bst1.put(2)
    bst1.put(6)
    bst1.put(10)
    bst2 = BST()
    # bst2.put(8)
    bst2.put(4)
    # bst2.put(12)
    bst2.put(2)
    bst2.put(6)
    # bst2.put(10)    
    print(check_subtree(bst1,bst2))

