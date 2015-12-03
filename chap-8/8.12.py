# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that
# none of them share the same row, column or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.

from pprint import pprint

def n_queens(n):
    ways = list()
    _n_queens(n, 0, list(), ways)
    return ways

def _n_queens(n, c, queens, ways):
    if c == n:
        ways.append(queens)
        return None
    for r in range(n):
        position = [ r, c ]
        if meet_requirements(position, queens):
            queens_cp = queens.copy()
            queens_cp.append(position)
            _n_queens(n, c+1, queens_cp, ways)

def meet_requirements(position, queens):
    for queen in queens:
        if queen[0] == position[0]:
            return False
        if queen[1] == position[1]:
            return False
        if (abs(queen[0] - position[0]) == abs(queen[1] - position[1])):
            return False
    return True

if __name__ == "__main__":
    for i in range(1, 11):
        ways = n_queens(i)
        print(len(ways))




