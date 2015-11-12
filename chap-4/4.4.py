# Implement a function to check if a binary tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node
# never differ by more than one.

class NodeBST(object):

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


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


# Time complexity: O(n^2*log(n)) (?)
def is_balanced_slow(bst):
    if bst is None:
        return None
    else:
        return _is_balanced_slow(bst.root)

# This is called 2*n times
def _is_balanced_slow(x):
    if x is None:
        return True
    if abs(_get_height_slow(x.left) - _get_height_slow(x.right)) <= 1:
        return _is_balanced_slow(x.left) and _is_balanced_slow(x.right)
    else:
        return False

# Time complexity: O(n*log(n))
def _get_height_slow(x):
    if x is None:
        return 0
    else:
        return max(_get_height_slow(x.left), _get_height_slow(x.right)) + 1


# Time complexity: O(n)
def is_balanced(bst):
    if bst is None:
        return None
    else:
        _, is_balanced = _is_balanced(bst.root)
        return is_balanced

def _is_balanced(x):
    if x is None:
        return (0, True)
    else:
        left_height, is_balanced = _is_balanced(x.left)
        right_height, is_balanced = _is_balanced(x.right)
        height = max(left_height, right_height) + 1
        if abs(left_height - right_height) <= 1 and is_balanced:
            return (height, True)
        else:
            return (height, False)


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
    print(is_balanced_slow(bst))
    print(is_balanced(bst))
    bst.put(16)
    bst.put(17)
    print(is_balanced_slow(bst))
    print(is_balanced(bst))

