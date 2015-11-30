# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes
# which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size
# from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
# constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto the next rod.
# (3) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first tower to the last using Stacks.

class Tower(object):

    def __init__(self, index):
        self.stack = list() # add: append(), remove: pop()
        self.index = index

    def add(self, n):
        if len(self.stack) != 0 and self.stack[-1] <= n:
            raise Exception("Cannot place disk in this tower.")
        else:
            self.stack.append(n)

    def move_top_to(self, t):
        t.add(self.stack.pop())

    def move_disks(self, n, dest, buff):
        if n > 0:
            self.move_disks(n-1, buff, dest)
            self.move_top_to(dest)
            buff.move_disks(n-1, dest, self)

def towers_of_hanoi(n):
    towers = [ Tower(i) for i in range(3) ]
    for i in range(n-1, -1, -1):
        towers[0].add(i)
    towers[0].move_disks(n, towers[2], towers[1])
    for t in towers:
        print(t.stack)

if __name__ == "__main__":
    towers_of_hanoi(9)
