# Given a sorted array of n integers that has been rotated an unknown number of times,
# write code to find an element in the array. You may assume that the array was originally sorted
# in increasing order.

def search(a, el):
    return _search(a, el, 0, len(a)-1)

def _search(a, el, lo, hi):
    if lo > hi:
        return None
    if el == a[mid]:
        return mid
    mid = (lo + hi) // 2
    if a[lo] < a[mid]: # left side is normally ordered
        if el < a[mid] and el > a[lo]: # go left
            return _search(a, el, lo, mid - 1)
        else: # go right
            return _search(a, el, mid + 1, hi)
    elif a[mid] < a[lo]: # right side is normally ordered
        if el > a[mid] and el < a[hi]: # go right
            return _search(a, el, mid + 1, hi)
        else: # go left
            return _search(a, el, lo, mid - 1)
    elif a[mid] == a[lo]: # all elements on the left are repeated
        if a[mid] != a[hi]: # go right
            return _search(a, el, mid + 1, hi)
        else: # must check both sides
            result = _search(a, el, lo, mid - 1) # try left
            if result is None:
                return _search(a, el, mid + 1, hi) # try right
            else:
                return result
    return None



