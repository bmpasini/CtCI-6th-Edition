def binary_search(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if x < a[mid]:
            hi = mid-1
        elif x > a[mid]:
            lo = mid+1
        else:
            return mid
    return None

if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7,8,9,10]
    print(binary_search(a,3))


def binary_search_rec(a, x):
    return _binary_search_rec(a, x, 0, len(a)-1)

def _binary_search_rec(a, x, lo, hi):
    if lo > hi:
        return None
    mid = lo + (hi-lo) // 2
    if x < a[mid]:
        return _binary_search_rec(a, x, lo, mid-1)
    elif x > a[mid]:
        return _binary_search_rec(a, x, mid+1, hi)
    else:
        return mid

if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7,8,9,10]
    print(binary_search(a,3))