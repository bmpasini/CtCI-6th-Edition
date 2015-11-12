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
        if key < x.key: # not do allow repeated elements (otherwise, use <=)
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
            return x

    # DFS

    def print_pre_order_traversal(self):
        self._print_pre_order_traversal(self.root)
        print(None)

    def _print_pre_order_traversal(self, x):
        if x is not None:
            print(x.key, "-> ", end="")
            self._print_pre_order_traversal(x.left)
            self._print_pre_order_traversal(x.right)

    def print_in_order_traversal(self):
        self._print_in_order_traversal(self.root)
        print(None)

    def _print_in_order_traversal(self, x):
        if x is not None:
            self._print_in_order_traversal(x.left)
            print(x.key, "-> ", end="")
            self._print_in_order_traversal(x.right)

    def print_post_order_traversal(self):
        self._print_post_order_traversal(self.root)
        print(None)

    def _print_post_order_traversal(self, x):
        if x is not None:
            self._print_post_order_traversal(x.left)
            self._print_post_order_traversal(x.right)
            print(x.key, "-> ", end="")

    # BFS

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


if __name__ == "__main__":
    t = BinarySearchTree()
    t.put('f', 6)
    t.put('b', 2)
    t.put('g', 7)
    t.put('a', 1)
    t.put('d', 4)
    t.put('i', 9)
    t.put('c', 3)
    t.put('e', 5)
    t.put('h', 8)
    print(t.get('a'))
    print(t.get('b'))
    print(t.get('c'))
    print(t.get('d'))
    print(t.get('e'))
    print(t.get('f'))
    print(t.get('g'))
    print(t.get('h'))
    print(t.get('i'))
    print(t.get('j'))
    t.print_pre_order_traversal()
    t.print_in_order_traversal()
    t.print_post_order_traversal()
    t.print_level_order_traversal()


