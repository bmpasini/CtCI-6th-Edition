class Node(object):

    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = None
        self.right = None

class BinaryTree(object):

    root = Node(10)
    root.left = Node(5)
    root.right = Node(-3)
    root.left.left = Node(3)
    root.left.right = Node(1)
    root.right.left = None
    root.right.right = Node(11)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right.left = None
    root.left.right.right = Node(2)
    # root.right.left.left = None
    # root.right.left.right = None
    root.right.right.left = None
    root.right.right.right = None

    def print_level_order(self):
        queue = [ self.root ] # insert left, remove right
        while len(queue) != 0:
            x = queue.pop()
            if x:
                print(x.data, "-> ", end="")
                queue.insert(0, x.left)
                queue.insert(0, x.right)
            elif len(queue) != 0:
                print(x, "-> ", end="")
        print(None)

# Time: O(n*log(n)) (if tree is balanced, otherwise worst case time complexity is O(n^2))
# Space: O(log(n)) (if tree is balanced, otherwise worst case space complexity is O(n)) 
def paths_with_sum_bf(bt, val):
    if bt is None:
        return None
    if bt.root is None:
        return 0
    return count_paths_with_sum_bf(bt.root, val)

def count_paths_with_sum_bf(x, target_sum):
    if x is None:
        return 0
    sum_root = count_paths_with_sum_from_root_bf(x, 0, target_sum)
    sum_left = count_paths_with_sum_bf(x.left, target_sum)
    sum_right = count_paths_with_sum_bf(x.right, target_sum)
    return sum_left + sum_root + sum_right

def count_paths_with_sum_from_root_bf(x, current_sum, target_sum):
    if x is None:
        return 0
    current_sum += x.data
    if current_sum == target_sum:
        total_paths = 1
    else:
        total_paths = 0
    total_paths += count_paths_with_sum_from_root_bf(x.left, current_sum, target_sum)
    total_paths += count_paths_with_sum_from_root_bf(x.right, current_sum, target_sum)
    return total_paths

# Time: O(n)
# Space: O(log(n)) (if tree is balanced, otherwise worst case space complexity is O(n^2))
def paths_with_sum(bt, val):
    if bt is None:
        return None
    if bt.root is None:
        return 0
    sums_table = { 0 : 1 }
    return count_paths_with_sum(bt.root, 0, val, sums_table)

def count_paths_with_sum(x, running_sum, target_sum, sums_table):
    if x is None:
        return 0
    running_sum += x.data
    try:
        sums_table[running_sum] += 1
    except KeyError:
        sums_table[running_sum] = 1
    try:
        total_paths = sums_table[running_sum - target_sum]
    except KeyError:
        total_paths = 0
    total_paths += count_paths_with_sum(x.left, running_sum, target_sum, sums_table)
    total_paths += count_paths_with_sum(x.right, running_sum, target_sum, sums_table)
    sums_table[running_sum] -= 1
    return total_paths

if __name__ == "__main__":
    bt = BinaryTree()
    bt.print_level_order()
    print(paths_with_sum_bf(bt, 8))
    print(paths_with_sum(bt, 8))






