def quicksort(a):
    return sort(a, 0, len(a)-1)

def sort(a, l, r):
    i = partition(a, l, r)
    if l < i-1:
        sort(a, l, i-1) # sort left
    if i < r:
        sort(a, i, r) # sort right

def partition(a, l, r):
    pivot = a[(l+r)//2]
    while l <= r:
        while a[l] < pivot:
            l += 1
        while a[r] > pivot:
            r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    return l


if __name__ == "__main__":
    a = [32,3,2,65,7,43,69,7,21,10,42,70]
    quicksort(a)
    print(a)