# Implement an algorithm to find the kth to last element of a singly linked list.

class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleList(object):

    head = None
    tail = None

    def show(self):
        x = self.head
        while x is not None:
            print(x.data, end='')
            print(" -> ", end='')
            x = x.next
        print(None)

    def append(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        prev = None
        x = self.head
        while x is not None:
            if x.data == node_value:
                if prev is not None:
                    prev.next = x.next
                else:
                    self.head = x.next
                break
            else:
                prev = x
                x = x.next
        if x.next is None:
            self.tail = x
        if self.head is None:
            self.tail = None

    def is_empty(self):
        return self.head is None

    def remove_duplicates_with_buffer(self):
        letters = {}
        x = self.head
        prev = None
        while x is not None:
            try:
                letters[x.data]
                prev.next = x.next
            except KeyError:
                letters[x.data] = True
                prev = x
            x = x.next

    def remove_duplicates(self):
        x = self.head
        runner = x
        while x is not None:
            while runner.next is not None:
                if x.data == runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            x = x.next
            runner = x

    def find_k_recursevely(self, k):
        return self.find_k_recurse(k, self.head)[0]

    def find_k_recurse(self, k, x):
        if x is None:
            return (None, 0)
        k_data, cnt = self.find_k_recurse(k, x.next)
        if cnt == k:
            return (x.data, cnt+1)
        else:
            return (k_data, cnt+1)

    def find_k_with_2_passes(self, k):
        cnt = 0
        x = self.head
        while x is not None:
            cnt += 1
            x = x.next
        k = cnt - k
        cnt = 0
        x = self.head
        while x is not None:
            cnt += 1
            if cnt == k:
                return x.data
            x = x.next
        return None

    def find_k(self, k):
        p1 = self.head
        p2 = self.head
        cnt = 0
        while cnt != k:
            cnt += 1
            p2 = p2.next
            if p2 is None:
                return None
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1.data


if __name__ == "__main__":
    ll = SingleList()
    ll.append("F")
    ll.append("O")
    ll.append("L")
    ll.append("L")
    ll.append("O")
    ll.append("W")
    ll.append(" ")
    ll.append("U")
    ll.append("P")
    ll.show()
    print(ll.find_k_recursevely(3))
    print(ll.find_k_with_2_passes(3))
    print(ll.find_k(3))
