# Implement a function to check if a binary tree is a binary search tree.

class NodeBST(object):

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class NodeBT(object):

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def insert_right(self, key):
        if self.root is None:
            self.root = NodeBT(key)
        elif self.root.right is None:
            self.root.right = NodeBT(key)
        else:
            tree = NodeBT(key)
            tree.right = self.root.right
            self.root.right = tree

    def insert_left(self, key):
        if self.root is None:
            self.root = NodeBT(key)
        elif self.root.left is None:
            self.root.left = NodeBT(key)
        else:
            tree = NodeBT(key)
            tree.left = self.root.left
            self.root.left = tree

    def print_level_order(self):
        queue = [ self.root ] # insert left, remove right
        while len(queue) != 0:
            x = queue.pop()
            if x:
                print(x.key, "-> ", end="")
                queue.insert(0, x.left)
                queue.insert(0, x.right)
            elif len(queue) != 0:
                print(x, "-> ", end="")
        print(None)

class BST(object):

    def __init__(self, root=None):
        self.root = root

    def put(self, key, val=None):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x is None:
            return NodeBST(key, val)
        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
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
            return self._get(x.left, key, val)
        elif key > x.key:
            return self._get(x.right, key, val)
        else:
            return x


# Assuming no repeated elements (if left elements and be equal the parent, change >= for >)
# Space complexity: O(n)
# Time complexity:  O(n)
def is_bst_bfs(bt):
    q = [ (bt.root, None, None) ] # add left, remove right // (node, min, max)
    while len(q) != 0:
        x, _min, _max = q.pop()
        if (_min is not None and x.key <= _min) or (_max is not None and x.key >= _max):
            return False
        if x.left:
            q.insert(0, (x.left, _min, x.key))
        if x.right:
            q.insert(0, (x.right, x.key, _max))
    return True

class Variable:
    v = None

# Assuming no repeated elements
# Space complexity: O(log(n))
# Time complexity:  O(n)
def is_bst_in_order(bt):
    last = Variable()
    return _is_bst_in_order(bt.root, last)

def _is_bst_in_order(x, last):
    if x is not None:
        if not _is_bst_in_order(x.left, last):
            return False
        if last.v is not None and x.key <= last.v:
            return False
        last.v = x.key
        if not _is_bst_in_order(x.right, last):
            return False
    return True

# Assuming no repeated elements (if left elements and be equal the parent, change >= for >)
# Space complexity: O(log(n))
# Time complexity:  O(n)
def is_bst_dfs(bt):
    return _is_bst_dfs(bt.root, None, None)

def _is_bst_dfs(x, _min, _max):
    if x is None:
        return True
    if (_min is not None and x.key <= _min) or (_max is not None and x.key >= _max):
        return False
    if not _is_bst_dfs(x.left, _min, x.key) or not _is_bst_dfs(x.right, x.key, _max):
        return False
    return True

class BT(object):

    root = NodeBST(20)
    root.left = NodeBST(10)
    root.right = NodeBST(30)
    # root.left.right = NodeBST(19)
    root.left.right = NodeBST(20)
    # root.left.right = NodeBST(25)

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
    print(is_bst_bfs(bst))
    print(is_bst_in_order(bst))
    print(is_bst_dfs(bst))
    t = BinaryTree()
    t.insert_left(1)
    t.insert_left(2)
    t.insert_right(3)
    t.insert_right(4)
    t.insert_left(5)
    t.insert_left(6)
    t.insert_right(7)
    t.insert_right(8)
    print(is_bst_bfs(t))
    print(is_bst_in_order(t))
    print(is_bst_dfs(t))
    bt = BT()
    print(is_bst_bfs(bt))
    print(is_bst_in_order(bt))
    print(is_bst_dfs(bt))


