def quicksort(a):
    return sort(a, 0, len(a)-1)

def sort(a, lo, hi):
    i = partition(a, lo, hi)
    if lo < i-1:
        sort(a, lo, i-1)
    if hi > i:
        sort(a, i, hi)

def partition(a, lo, hi):
    pivot = a[(lo + hi) // 2]
    while lo <= hi:
        while a[lo] < pivot:
            lo += 1
        while a[hi] > pivot:
            hi -= 1
        if lo <= hi:
            a[lo], a[hi] = a[hi], a[lo]
            lo += 1
            hi -= 1
    return lo

if __name__ == "__main__":
    a = [32,3,2,65,7,43,69,7,21,10,42,70]
    quicksort(a)
    print(a)