# Check if a linked list is palindrome

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = Node(data)

class Stack(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head is None:
            return None
        old_head = self.head
        self.head = old_head.next
        return old_head.data

    def peek(self, data):
        return self.head

def print_ll(head):
    while head:
        print(head.data, "-> ", end= "")
        head = head.next
    print(None)

def is_palindrome_recursive(head):
    x = head
    runner = head
    while runner.next and runner.next.next:
        x = x.next
        runner = runner.next.next 
    _, result = check_palindrome(head, x)
    return result
    
def check_palindrome(x1, x2):
    if x2.next is None:
        return (x1, True)
    x2 = x2.next
    x1, _ = check_palindrome(x1, x2)
    if x1 and x2.data == x1.data:
        return (x1.next, True)
    else:
        return (None, False)

def is_palindrome_iterative(head):
    s = Stack()
    x = head
    runner = head
    while runner.next and runner.next.next:
        s.push(x)
        x = x.next
        runner = runner.next.next
    if runner.next is not None: # even
        s.push(x)
    x = x.next
    while x:
        if s.pop().data != x.data:
            return False
        x = x.next
    return True

def is_palindrome_reverse(head):
    reverse = reverse_list(head)
    x = head
    runner = head
    while runner.next and runner.next.next:
        x = x.next
        reverse = reverse.next
        runner = runner.next.next
        if x.data != reverse.data:
            return False
    return True

def reverse_list(head):
    from copy import copy
    prev = None
    x = copy(head)
    while x:
        next = copy(x.next)
        x.next = prev
        prev = x
        x = next
    return prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    # ll.append(4)
    ll.append(3)
    # ll.append(2)
    ll.append(1)
    print_ll(ll.head)
    print(is_palindrome_recursive(ll.head))
    print(is_palindrome_iterative(ll.head))
    print_ll(reverse_list(ll.head))
    print_ll(ll.head)
    print(is_palindrome_reverse(ll.head))



