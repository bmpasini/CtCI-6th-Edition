def selectionsort(a):
    for i in range(len(a)):
        i_min = i
        for j in range(i+1, len(a)):
            if a[j] < a[i_min]:
                i_min = j
        if i_min != i:
            a[i], a[i_min] = a[i_min], a[i]

if __name__ == "__main__":
  a = [32,3,2,65,7,43,69,7,21,10,42,70]
  selectionsort(a)
  print(a)



