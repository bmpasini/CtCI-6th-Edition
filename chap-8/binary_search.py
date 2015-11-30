def binary_search(a, n):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == n:
            return mid
        elif a[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7,8,9,10]
    print(binary_search(a,3))