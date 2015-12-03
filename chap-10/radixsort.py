def radixsort(a):
    RADIX = 10
    max_length = False
    tmp = -1
    place = 1
    while not max_length:
        max_length = True
        buckets = [ list() for _ in range(RADIX) ]
        for item in a:
            tmp = item // place
            buckets[tmp % RADIX].append(item)
            if max_length and tmp > 0:
                max_length = False
        i = 0
        for bucket in buckets:
            for item in bucket:
                a[i] = item
                i += 1
        place *= RADIX
        print(buckets, a)

if __name__ == "__main__":
  a = [32,3,2,65,7,43,69,7,21,10,42,70]
  radixsort(a)
  print(a)



