class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
        self.size += 1

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val)
        else:
            if key < x.key: # not do allow repeated elements (otherwise, use <=)
                x.left = self._put(x.left, key, val)
            elif key > x.key:
                x.right = self._put(x.right, key, val)
            else:
                x.val = val
            return x

    def get(self, key):
        return self._get(self.root, key, val).val

    def _get(self, x, key):
        if x is None:
            return None
        else:
            if key < x.key:
                return self._get(x.left, key)
            elif key > x.key:
                return self._get(x.right, key)
            else:
                return x

