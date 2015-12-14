# In an array of integers, a "peak" is an element which is greater than or equal to the adjacent
# integers and a "valley" is an element which is less than or equal to the adjacent integers. For
# example, in the array [5, 8, 6, 2, 3, 4, 6], [8, 6] are peaks and [5, 2] are valleys. Given an
# array of integers, sort the array into an alternating sequence of peaks and valleys.

# Time complexity: O(n*log(n))
# Space complexity: O(1)
def peaks_and_valleys(a):
    a.sort()
    for i in range(1, len(a), 2):
        a[i-1], a[i] = a[i], a[i-1]

if __name__ == "__main__":
    a = [5, 8, 6, 2, 3, 4, 6]
    peaks_and_valleys(a)
    print(a)
    a = [0, 1, 4, 7, 8, 9]
    peaks_and_valleys(a)
    print(a)
    a = [5, 3, 1, 2, 3]
    peaks_and_valleys(a)
    print(a)

# Time complexity: O(n)
# Space complexity: O(1)
def peaks_and_valleys(a):
    for i in range(0, len(a), 2):
        _max = max_index(a, i-1, i, i+1)
        if _max != i:
            a[i], a[_max] = a[_max], a[i]

def max_index(_list, a, b, c):
    a_val = within_boundary(_list, a)
    b_val = within_boundary(_list, b)
    c_val = within_boundary(_list, c)
    _max = max(a_val, max(b_val, c_val))
    if _max == a_val:
        return a
    elif _max == b_val:
        return b
    else:
        return c

def within_boundary(_list, a):
    if a >= 0 and a < len(_list):
        return _list[a]
    else:
        return -sys.maxsize-1

if __name__ == "__main__":
    import sys
    a = [5, 8, 6, 2, 3, 4, 6]
    peaks_and_valleys(a)
    print(a)
    a = [0, 1, 4, 7, 8, 9]
    peaks_and_valleys(a)
    print(a)
    a = [5, 3, 1, 2, 3]
    peaks_and_valleys(a)
    print(a)
