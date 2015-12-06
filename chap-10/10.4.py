# You are given an array-like data structure Listy which lacks a size method. It does, however,
# have an elementAt(i) method that returns the element at index i in O(1) time. If i is beyond the
# bounds of the data structure, it returns -1. (For this reason, the data structure only supports
# positive integers). Given a Listy which contains sorted, positive integers, find the index at
# which an element x occurs. If x occurs multiple times, you may return any index.

# Use a list, but don't use the len() method.
# Time: O(log^2(n))
def binary_search(listy, x):
    if listy[0] == -1:
        return None
    lo = 0
    hi = find_size(listy)
    while lo <= hi:
        mid = (lo + hi) // 2
        if x < listy[mid]:
            hi = mid-1
        elif x > listy[mid]:
            lo = mid+1
        else:
            return mid
    return None

def find_size(listy, i=0, delta=1):
    if listy[i+delta] == -1 and listy[i+delta-1] != -1:
        return i+delta-1
    elif listy[i+delta] != -1:
        return find_size(listy, i, 2*delta)
    else:
        return find_size(listy, i+delta//2, 1)

if __name__ == "__main__":
    listy = [0,1,2,3,4,5,6,7,-1]
    print(find_size(listy))
    print(binary_search(listy, 7))


def binary_search(listy, x):
    i = 1
    while listy[i] != -1 and listy[i] < x:
        i *= 2
    return _binary_search(listy, x, i // 2, i)

def _binary_search(listy, x, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if x < listy[mid] or listy[mid] == -1:
            hi = mid-1
        elif x > listy[mid]:
            lo = mid+1
        else:
            return mid
    return None


if __name__ == "__main__":
    listy = [0,1,2,3,4,5,6,7,-1]
    print(binary_search(listy, 7))





