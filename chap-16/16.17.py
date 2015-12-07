# You are given an array of integers (both positive and negative). Find the contiguous sequence with the
# largest sum. Return the sum.

def contiguous_sequence(seq):
    max_start = 0
    max_end = 0
    max_sum = 0
    current_start = 0
    current_sum = 0
    for i, el in enumerate(seq):
        if current_sum == 0:
            current_start = i
            current_sum = el
        else:
            current_sum += el
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i
        if current_sum < 0:
            current_sum = 0
    return max_sum, seq[max_start:(max_end+1)]

if __name__ == "__main__":
    i = [ -8, 3, -2, 4, -10 ]
    print(contiguous_sequence(i))


def contiguous_sequence(seq):
    max_sum = 0
    _sum = 0
    for el in seq:
        _sum += el
        if _sum > max_sum:
            max_sum = _sum
        elif _sum < 0:
            _sum = 0
    return max_sum

if __name__ == "__main__":
    i = [ -8, 3, -2, 4, -10 ]
    print(contiguous_sequence(i))

