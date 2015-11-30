# A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index,
# if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?

def magic_index_rec(a):
    return _magic_index_rec(a, 0, len(a)-1)

def _magic_index_rec(a, lo, hi):
    if hi < lo or lo < 0 or hi >= len(a):
        return None
    mid = lo + (hi - lo) // 2
    if a[mid] == mid:
        return mid
    elif a[mid] < mid:
        return _magic_index_rec(a, mid+1, hi)
    else:
        return _magic_index_rec(a, lo, mid-1)

def magic_index(a):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == mid:
            return mid
        elif a[mid] < mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

def magic_index_slow(a):
    i = 0
    while a[i] < len(a):
        if i == a[i]:
            return i
        i += 1
    return None

# FOLLOW UP
# What if the values are not distinct?

def magic_index_fu(a):
    return _magic_index_fu(a, 0, len(a)-1)

def _magic_index_fu(a, lo, hi):
    if hi < lo or lo < 0 or hi >= len(a):
        return None
    mid = lo + (hi - lo) // 2
    if a[mid] == mid:
        return mid
    # check left
    left_hi = min(mid-1, a[mid])
    left = _magic_index_fu(a, lo, left_hi)
    if left is not None:
        return left
    # check right
    right_lo = max(mid+1, a[mid])
    return _magic_index_fu(a, right_lo, hi)
    

if __name__ == "__main__":
    a = [-10,-5,2,2,2,3,4,7,9,12,13]
    print(magic_index_slow(a))
    print(magic_index(a))
    print(magic_index_rec(a))
    print(magic_index_fu(a))

    