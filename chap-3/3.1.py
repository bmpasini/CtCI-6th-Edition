# use a single array to implement 3 stacks

class ThreeStacks(object):

    def __init__(self, size_of_stack):
        self.stack_list = [ None for _ in range(3 * size_of_stack) ]
        self.p = [0, 100, 200]

    def push(self, stack_index, data):
        if self.p[stack_index] == 100 * stack_index + 100:
            raise Exception("Stack is full.")
        else:
            self.stack_list[self.p[stack_index]] = data
            self.p[stack_index] += 1

    def pop(self, stack_index):
        if self.is_empty(stack_index):
            raise Exception("Stack is empty.")
        else:
            data = self.stack_list[self.p[stack_index]]
            self.stack_list[self.p[stack_index]] = None
            self.p[stack_index] -= 1
            return data

    def peek(self, stack_index):
        if self.is_empty(stack_index):
            raise Exception("Stack is empty.")
        else:
            return self.stack_list[self.p[stack_index]]

    def is_empty(self, stack_index):
        return self.p[stack_index] == 100 * stack_index


if __name__ == "__main__":
    s = ThreeStacks(100)
    # s.peek(0)
    for i in range(100):
        s.push(0, i)
    for i in range(100):
        print(s.pop(0))
    print(s.is_empty(0))
    s.pop(1)

