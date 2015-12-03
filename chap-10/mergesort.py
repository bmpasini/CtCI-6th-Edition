def mergesort(array):
    return sort(array, [None]*len(array), 0, len(array)-1)


def sort(array, helper, lo, hi):
    if lo < hi:
        mid = (lo + hi) // 2
        sort(array, helper, lo, mid) # sort left
        sort(array, helper, mid+1, hi) # sort right
        merge(array, helper, lo, mid, hi) # merge them

def merge(array, helper, lo, mid, hi):
    for i in range(lo, hi+1):
        helper[i] = array[i]
    l = lo
    r = mid + 1
    i = lo
    while l <= mid and r <= hi:
        if helper[l] <= helper[r]:
            array[i] = helper[l]
            l += 1
        else:
            array[i] = helper[r]
            r += 1
        i += 1
    for j in range(mid-l+1):
        array[i+j] = helper[l+j]


if __name__ == "__main__":
    a = [32,3,2,65,7,43,69,7,21,10,42,70]
    mergesort(a)
    print(a)

