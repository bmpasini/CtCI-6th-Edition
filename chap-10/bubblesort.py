def bubblesort(a):
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,n):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                swapped = True
        n -= 1

if __name__ == "__main__":
  a = [32,3,2,65,7,43,69,7,21,10,42,70]
  bubblesort(a)
  print(a)

# optimization
def bubblesort(a):
    n = len(a)
    while n != 0:
        new_n = 0
        for i in range(1,n):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                new_n = i
        n = new_n

if __name__ == "__main__":
  a = [32,3,2,65,7,43,69,7,21,10,42,70]
  bubblesort(a)
  print(a)