from random import random
from math import floor

class Node(object):

    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = None
        self.right = None


class BinaryTree(object):

    root = None

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size

    def insert_in_order(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_in_order(self.root, data)

    def _insert_in_order(self, x, data):
        if data <= x.data:
            if x.left is not None:
                self._insert_in_order(x.left, data)
            else:
                x.left = Node(data)
        else:
            if x.right is not None:
                self._insert_in_order(x.right, data)
            else:
                x.right = Node(data)
        x.size += 1

    def find(self, data):
        if self.root is None:
            return None
        else:
            return self._find(self.root, data)

    def _find(self, x, data):
        if data == x.data:
            return x
        if data < x.data and x.left:
            return self._find(x.left, data)
        elif data > x.data and x.right:
            return self._find(x.right, data)
        else:
            return None

    def get_random_node(self):
        if self.root is None:
            return None
        else:
            return self._get_random_node(self.root)

    def _get_random_node(self, x):
        if x.left:
            size_left = x.left.size
        else:
            size_left = 0
        index = floor(x.size * random())
        if index < size_left:
            return self._get_random_node(x.left)
        elif index == size_left:
            return x
        else:
            return self._get_random_node(x.right)

    def get_random_node2(self):
        if self.root is None:
            return None
        else:
            index = floor(self.root.size * random())    
            return self.get_ith_node(self.root, index)

    def get_ith_node(self, x, index):
        if x.left:
            size_left = x.left.size
        else:
            size_left = 0
        if index < size_left:
            return self.get_ith_node(x.left, index)
        elif index == size_left:
            return x
        else:
            return self.get_ith_node(x.right, index - (1 + size_left))


if __name__ == "__main__":
    bst = BinaryTree()
    bst.insert_in_order(8)
    bst.insert_in_order(4)
    bst.insert_in_order(12)
    bst.insert_in_order(2)
    bst.insert_in_order(6)
    bst.insert_in_order(10)
    bst.insert_in_order(14)
    bst.insert_in_order(1)
    bst.insert_in_order(3)
    bst.insert_in_order(5)
    bst.insert_in_order(7)
    bst.insert_in_order(9)
    bst.insert_in_order(11)
    bst.insert_in_order(13)
    bst.insert_in_order(15)
    print(bst.get_random_node2().data)





