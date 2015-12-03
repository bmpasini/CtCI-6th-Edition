# Given a sequence of N numbers – A[1] , A[2] , …, A[N] . Find the length of the longest
# non-decreasing sequence.

def length_of_longest_non_decreasing_sequence(seq):
    i = 0
    prev = float("-inf")
    for el in seq:
        if el >= prev:
            i += 1
        prev = el
    return i

print(length_of_longest_non_decreasing_sequence([5,3,4,8,6,7]))
