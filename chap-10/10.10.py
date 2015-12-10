# Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the
# rank of a number x (the number of values less than or equal to x). Implement the data structures and
# algorithms to support these operations. That is, implement the method track(int x), which is called
# when each number is generated, and the method getRankOfNumber(int x), which returns the number of
# values less than or equal to x (not including x itself).
# EXAMPLE
# Stream (inorder of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3

# Assuming that x may or may not have appeared before in the tree
# Time complexity:
    # Track: O(log(n))
    # Get Rank: O(n)
# Space complexity: O(n)

class Node_v1(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST_v1(object):

    def __init__(self, root=None):
        self.root = root

    def track(self, data):
        if self.root is None:
            self.root = Node_v1(data)
        else:
            self.root = self._track(self.root, data)

    def _track(self, x, data):
        if x is None:
            return Node_v1(data)
        if data <= x.data:
            x.left = self._track(x.left, data)
        else:
            x.right = self._track(x.right, data)
        return x

    def get_rank_of_number(self, data):
        if self.root is None:
            return None
        return self._get_rank_of_number(self.root, data)

    def _get_rank_of_number(self, x, data, found=False):
        if x is None:
            return 0
        if data <= x.data and not found:
            if data == x.data:
                found = True
            return self._get_rank_of_number(x.left, data, found)
        elif data <= x.data:
            return 1 + self._get_rank_of_number(x.left, data, found)
        else:
            return 1 + self._get_rank_of_number(x.left, data, found) \
                     + self._get_rank_of_number(x.right, data, found)


if __name__ == "__main__":
    bst = BST_v1()
    stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
    for data in stream:
        bst.track(data)
    print(bst.get_rank_of_number(4)) # 3
    print(bst.get_rank_of_number(5)) # 5
    print(bst.get_rank_of_number(9)) # 7
    print(bst.get_rank_of_number(7)) # 6
    print(bst.get_rank_of_number(13)) # 8
    print(bst.get_rank_of_number(3)) # 1
    print(bst.get_rank_of_number(1)) # 0
    print()


# Time complexity:
    # Track:    O(log(n))
    # Get Rank: O(log(n))
# Space complexity: O(n)

class Node_v2(object):

    def __init__(self, data, left_count=0):
        self.data = data
        self.left_count = left_count
        self.left = None
        self.right = None

class BST_v2(object):

    def __init__(self, root=None):
        self.root = root

    def track(self, data):
        if self.root is None:
            self.root = Node_v2(data)
        else:
            self.root = self._track(self.root, data)

    def _track(self, x, data):
        if x is None:
            return Node_v2(data)
        if data <= x.data:
            x.left = self._track(x.left, data)
            x.left_count += 1
        else:
            x.right = self._track(x.right, data)
        return x

    def get_rank_of_number(self, data):
        if self.root is None:
            return None
        return self._get_rank_of_number(self.root, data)

    def _get_rank_of_number(self, x, data):
        if x is None:
            return None
        if data == x.data:
            return x.left_count
        elif data < x.data:
            return self._get_rank_of_number(x.left, data)
        else:
            right_count = self._get_rank_of_number(x.right, data)
            if right_count is None:
                return None
            return x.left_count + 1 + right_count        


if __name__ == "__main__":
    bst = BST_v2()
    stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
    for data in stream:
        bst.track(data)
    print(bst.get_rank_of_number(4)) # 3
    print(bst.get_rank_of_number(5)) # 5
    print(bst.get_rank_of_number(9)) # 7
    print(bst.get_rank_of_number(7)) # 6
    print(bst.get_rank_of_number(13)) # 8
    print(bst.get_rank_of_number(3)) # 1
    print(bst.get_rank_of_number(1)) # 0


import unittest

class Test(unittest.TestCase):

    def test_get_rank_of_number_v1(self):
        bst = BST_v1()
        stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
        for data in stream:
            bst.track(data)
        self.assertEqual(bst.get_rank_of_number(4), 3)
        self.assertEqual(bst.get_rank_of_number(5), 5)
        self.assertEqual(bst.get_rank_of_number(9), 7)
        self.assertEqual(bst.get_rank_of_number(7), 6)
        self.assertEqual(bst.get_rank_of_number(13), 8)
        self.assertEqual(bst.get_rank_of_number(3), 1)
        self.assertEqual(bst.get_rank_of_number(1), 0)

    def test_get_rank_of_number_v2(self):
        bst = BST_v2()
        stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
        for data in stream:
            bst.track(data)
        self.assertEqual(bst.get_rank_of_number(4), 3)
        self.assertEqual(bst.get_rank_of_number(5), 5)
        self.assertEqual(bst.get_rank_of_number(9), 7)
        self.assertEqual(bst.get_rank_of_number(7), 6)
        self.assertEqual(bst.get_rank_of_number(13), 8)
        self.assertEqual(bst.get_rank_of_number(3), 1)
        self.assertEqual(bst.get_rank_of_number(1), 0)


if __name__ == "__main__":
    print("\nUNIT TESTS:\n")
    unittest.main()




