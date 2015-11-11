# Imagine a (literal) stack of plates. If the stack gets too high,
# it might topple. Therefore, in real life, we would likely start
# a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and should
# create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks. pop () should behave
# identically to a single stack (that is, pop () should return
# the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation
# on a specific sub-stack.

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def push(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty.")
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            raise Exception("Stack is empty.")
        else:
            return self.head.data

    def get_size(self):
        return self.size

    def get_real_size(self):
        size = 0
        x = self.head
        while x:
            size += 1
            x = x.next
        return size

    def print_stack(self):
        x = self.head
        while x:
            print(x.data, "-> ", end="")
            x = x.next
        # print(None)


class SetOfStacks(object):

    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks = [Stack()]

    def push(self, data):
        if len(self.stacks) == 0 or self.stacks[-1].get_size() == self.stack_capacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(data)

    def pop(self):
        if len(self.stacks) == 0:
            raise Exception("Stack is empty.")
        data = self.stacks[-1].pop()
        if self.stacks[-1].get_size() == 0:
            self.stacks.pop()
        return data

    # leave stacks half-full
    def popAtHalfFull(self, index):
        if len(self.stacks) == 0:
            raise Exception("Stack is empty.")
        if index > len(self.stacks) - 1:
            raise IndexError("Index out of range.")
        else:
            data = self.stacks[index].pop()
            if self.stacks[index].get_size() == 0:
                del self.stacks[index]
            return data

    # full implementation
    def popAt(self, index):
        if len(self.stacks) == 0:
            raise Exception("Stack is empty.")
        if index > len(self.stacks) - 1:
            raise IndexError("Index out of range.")
        else:
            data = self.stacks[index].pop()
            if self.stacks[index].get_size() == 0:
                del self.stacks[index]
            else:
                self.reorder_stacks(index)
            return data

    def reorder_stacks(self, index):
        while index < len(self.stacks) - 1:
            prev = None
            x = self.stacks[index+1].head
            if x.next:
                while x.next:
                    prev = x
                    x = x.next
                prev.next = x.next
            else:
                del self.stacks[index+1]
            self.stacks[index].push(x.data)
            index += 1

    def print_stack(self):
        i = len(self.stacks)
        while i > 0:
            stack = self.stacks[i-1]
            i -= 1
            x = stack.head
            while x:
                print(x.data, "-> ", end="")
                x = x.next
        print(None)

if __name__ == "__main__":
    s = SetOfStacks(10)
    for i in range(101):
        s.push(i)
    for i in range(101):
        print(s.pop())
    # print(len(s.stacks))
    s = SetOfStacks(10)
    for i in range(101):
        s.push(i)
    s.print_stack()
    print(s.stacks[10].print_stack())
    print(s.popAt(0))
    s.print_stack()
    print(s.stacks[0].print_stack())
    print(s.stacks[1].print_stack())
    print(s.stacks[8].print_stack())
    print(s.stacks[9].print_stack())
    # print(s.popAt(1))
    # print(s.popAt(2))
    # print(s.popAt(3))
    # print(s.popAt(4))
    # print(s.popAt(5))
    # print(s.popAt(6))
    # print(s.popAt(7))
    # print(s.popAt(8))
    # print(s.popAt(9))
    # print(s.popAt(9))






