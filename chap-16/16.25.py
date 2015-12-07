# Design and build a "least recently used" cache, which evicts the least recently used item. The cache
# should map from keys to values (allow you to insert and retrieve a value associated with a particular
# key) and be initialized with a max size. When it is full, it should evict the least recently used
# item.

class LRU(object):

    def __init__(self, size):
        self.size = size
        self.ordered_items = DoublyLinkedList()
        self.map = dict()

    def update(self, key):
        self.ordered_items.remove(key)
        self.ordered_items.insert_first(key)

    def insert(self, key, val):
        if self.ordered_items.get(key):
            self.update(key)
            self.map[key] = val
        else:
            if len(self.map) == size:
                last = self.ordered_items.remove_last()
                del self.map[last]
            self.ordered_items.insert_first(key)
            self.map[key] = val

    def retrieve(self, key):
        if self.ordered_items.get(key):
            self.update(key)
            return self.map[key]
        else:
            return None



