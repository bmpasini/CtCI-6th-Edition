
class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = Node(data)

def print_ll(head):
    while head:
        print(head.data, "-> ", end= "")
        head = head.next
    print(None)

# space: O(n)
# time: O(largest_list) 
def sum_lists(h1, h2):
    head = None
    carry = 0
    while h1 and h2:
        s = h1.data + h2.data + carry
        carry = s // 10
        s = s % 10
        if head is None:
            head = Node(s)
            x = head
        else:
            x.next = Node(s)
            x = x.next
        h1 = h1.next
        h2 = h2.next
    carry = keep_summing(h1, x, carry)
    carry = keep_summing(h2, x, carry)
    if carry != 0:
        x.next = Node(carry)
    return head

def keep_summing(h, head, carry):
    while h:
        s = h.data + carry
        carry = s // 10
        s = s % 10
        head.next = Node(s)
        h = h.next
        head = head.next
    return carry

def sum_lists_recursevely(h1, h2, carry):
    result = Node(0)
    if h1 is None and h2 is None and carry == 0:
        return None
    val = carry
    if h1 is not None:
        val += h1.data
        h1 = h1.next
    if h2 is not None:
        val += h2.data
        h2 = h2.next
    carry = val // 10
    result.data = val % 10
    result.next = sum_lists_recursevely(h1, h2, carry)
    return result

def add_to_front(ll, data):
    # add_to_front_node(ll.head, data)
    ll.head = Node(data, ll.head)

def add_to_front_node(h, data):
    return Node(data, h)

def sum_lists_not_reversed_helper(h1, h2):
    result = Node(0)
    if h1.next is None and h2.next is None:
        val = h1.data + h2.data
        result.data = val % 10
        return (result, val // 10)
    result.next, carry = sum_lists_not_reversed_helper(h1.next, h2.next)
    val = carry + h1.data + h2.data
    result.data = val % 10
    return (result, val // 10)

def pad_list(ll, n):
    while n != 0:
        add_to_front(ll, 0)

def length(h):
    i = 0
    while h:
        i += 1
        h = h.next
    return i

def sum_lists_not_reversed_recursively(ll1, ll2, carry):
    h1 = ll1.head
    h2 = ll2.head
    l1 = length(h1)
    l2 = length(h2)
    if l1 > l2:
        pad_list(ll1,l1-l2)
    elif l1 < l2:
        pad_list(ll2,l2-l1)
    result, carry = sum_lists_not_reversed_helper(h1, h2)
    if carry != 0:
        return add_to_front_node(result, carry)
    else:
        return result

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(7)
    ll1.append(8)
    ll1.append(2)
    ll2 = LinkedList()
    ll2.append(4)
    ll2.append(3)
    ll2.append(8)
    ll3 = sum_lists(ll1.head,ll2.head)
    print_ll(ll3)
    print_ll(sum_lists_recursevely(ll1.head, ll2.head, 0))
    print_ll(sum_lists_not_reversed_recursively(ll1, ll2, 0))



