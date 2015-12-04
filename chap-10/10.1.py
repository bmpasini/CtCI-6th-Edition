# You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

# Time: O(a)
# Space: O(a)
def sorted_merge(a, b):
    merge(a, b, [None] * len(a))

def merge(a, b, a_helper):
    for i in range(len(a)):
        a_helper[i] = a[i]
    ah_i = 0
    b_i = 0
    a_i = 0
    while b_i < len(b):
        if a_helper[ah_i] is not None and a_helper[ah_i] <= b[b_i]:
            a[a_i] = a_helper[ah_i]
            ah_i += 1
        else:
            a[a_i] = b[b_i]
            b_i += 1
        a_i += 1
    i = 0
    while a_helper[ah_i+i] is not None:
        a[a_i+i] = a_helper[ah_i+i]
        i += 1

if __name__ == "__main__":
    a = [2,4,6,7,None,None,None,None]
    b = [1,3,5]
    sorted_merge(a,b)
    print(a)

# This solution assumes that array A fits array B perfectly (it becomes a full array).
# Time: O(a)
# Space: O(1)
def sorted_merge(a, b):
    merge(a, b, len(a)-len(b)-1, len(b)-1)

def merge(a, b, last_a_i, last_b_i):
    a_i = last_a_i
    b_i = last_b_i
    i = last_a_i + last_b_i + 1
    while a_i >= 0 and b_i >= 0:
        if a[a_i] >= b[b_i]:
            a[i] = a[a_i]
            a_i -= 1
        else:
            a[i] = b[b_i]
            b_i -= 1
        i -= 1
    while b_i >= 0:
        a[i] = b[b_i]
        b_i -= 1
        i -= 1

if __name__ == "__main__":
    a = [2,4,6,7,None,None,None,None]
    b = [1,3,5,8]
    sorted_merge(a,b)
    print(a)






