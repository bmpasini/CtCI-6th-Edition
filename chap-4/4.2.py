# Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST(object):

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
        self.size += 1
        return self.root

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val)
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
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return val

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

class MinimalBST(BST):

    def put_ary(self, ary):
        if ary is not None:
            self.root = self._put_ary(ary, 0, len(ary)-1)
            return self.root

    def _put_ary(self, ary, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        x = Node(ary[mid], None)
        x.left = self._put_ary(ary, start, mid-1)
        x.right = self._put_ary(ary, mid+1, end)
        return x


if __name__ == "__main__":
    t = MinimalBST()
    ary = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    t.put_ary(ary)
    t.print_level_order()


# binary search
def create(bst, a):
    _create(bst, a, 0, len(a)-1)

def _create(bst, a, lo, hi):
    if lo <= hi:
        mid = (lo + hi) // 2
        bst.put(a[mid], 0)
        _create(bst, a, mid+1, hi)
        _create(bst, a, lo, mid-1)

if __name__ == "__main__":
    t = BST()
    ary = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    create(t, ary)
    t.print_level_order()

