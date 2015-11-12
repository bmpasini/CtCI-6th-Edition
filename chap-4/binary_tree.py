class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def insert_right(self, val):
        if self.root is None:
            self.root = Node(val)
        elif self.root.right is None:
            self.root.right = Node(val)
        else:
            tree = Node(val)
            tree.right = self.root.right
            self.root.right = tree

    def insert_left(self, val):
        if self.root is None:
            self.root = Node(val)
        elif self.root.left is None:
            self.root.left = Node(val)
        else:
            tree = Node(val)
            tree.left = self.root.left
            self.root.left = tree

    def print_level_order(self):
        queue = [ self.root ] # insert left, remove right
        while len(queue) != 0:
            x = queue.pop()
            if x:
                print(x.val, "-> ", end="")
                queue.insert(0, x.left)
                queue.insert(0, x.right)
            elif len(queue) != 0:
                print(x, "-> ", end="")
        print(None)


if __name__ == "__main__":
    t = BinaryTree()
    t.insert_left(1)
    t.insert_left(2)
    t.insert_right(3)
    t.insert_right(4)
    t.insert_left(5)
    t.insert_left(6)
    t.insert_right(7)
    t.insert_right(8)
    t.print_level_order()
        

