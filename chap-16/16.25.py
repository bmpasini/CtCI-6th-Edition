# Design and build a "least recently used" cache, which evicts the least recently used item. The cache
# should map from keys to values (allow you to insert and retrieve a value associated with a particular
# key) and be initialized with a max size. When it is full, it should evict the least recently used
# item.

class DLLNode(object):
    
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRU(object):

    def __init__(self, size):
        self.size = size
        self.head = None
        self.tail = None
        self.map = dict()

    def insert(self, key, val):
        if self.head is None or self.tail is None:
            node = self.head = self.tail = DLLNode(key, val)
            self.map[key] = node
        else:
            if len(self.map) == self.size:
                del self.map[self.tail.key]
                self.tail = self.tail.left
                self.tail.right = None
            self.update(key, val)

    def update(self, key, val):
        if self.map.get(key):
            node = self.map[key]
            self.remove_node(node)
            node.key = key
            node.val = val
        else:
            node = DLLNode(key, val)
        node.left = None
        node.right = self.head
        self.head.left = self.map[key] = node
        self.head = node
            
    def remove_node(self, node):
        if node is None:
            return None
        elif node == self.head:
            self.head = self.head.right
        elif node == self.tail:
            self.tail = self.tail.left
        else:
            left = node.left
            right = node.right
            if left is not None:
                left.right = right
            if right is not None:
                right.left = left

    def retrieve(self, key):
        if self.map.get(key):
            val = self.map[key].val
            self.update(key, val)
            return val
        else:
            return None


if __name__ == "__main__":
    lru = LRU(4)
    lru.insert(72, 'Food')
    lru.insert(13, 'Keychain')
    lru.insert(45, 'Blanket')
    lru.insert(27, 'Book')
    print(lru.retrieve(72))
    lru.insert(42, 'Hemorroids')
    print(lru.retrieve(13))
    for k, v in lru.map.items():
        print(k, v.val)
    











