# Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation.

def find_next_arithmetically(n):
    c = n
    c0 = 0
    c1 = 0
    while ((c & 1) == 0 and c != 0):
        c0 += 1
        c >>= 1
    while ((c & 1) == 1):
        c1 += 1
        c >>= 1
    if c0 + c1 == 53 or c0 + c1 == 0:
        return -1
    return n + (1 << c0) + (1 << (c1 - 1)) - 1

print(bin(find_next_arithmetically(int('0b011011001111100', 2))))

def find_prev_arithmetically(n):
    c = n
    c0 = 0
    c1 = 0
    while ((c & 1) == 1):
        c1 += 1
        c >>= 1
    if c == 0:
        return -1
    while ((c & 1) == 0 and c != 0):
        c0 += 1
        c >>= 1
    return n - ((1 << c1) - 1) - 1 - ((1 << (c0 - 1)) - 1)

print(bin(find_prev_arithmetically(int('0b10011110000011', 2))))

def find_next(n):
    c = n
    c0 = 0
    c1 = 0
    while ((c & 1) == 0 and c != 0):
        c0 += 1
        c >>= 1
    while ((c & 1) == 1):
        c1 += 1
        c >>= 1
    if c0 + c1 == 53 or c0 + c1 == 0:
        return -1
    p = c0 + c1
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= ((1 << (c1 - 1)) - 1)
    return n

print(bin(find_next(int('0b011011001111100', 2))))

def find_prev(n):
    c = n
    c0 = 0
    c1 = 0
    while ((c & 1) == 1):
        c1 += 1
        c >>= 1
    if c == 0:
        return -1
    while ((c & 1) == 0 and c != 0):
        c0 += 1
        c >>= 1
    p = c0 + c1
    n &= (~0 << (p + 1))
    n |= (((1 << (c1 + 1)) - 1) << (c0 - 1))
    return n

print(bin(find_prev(int('0b10011110000011', 2))))

def find_next2(n):
    cnt_zeros = 0
    found_one = False
    for i, c in enumerate(n[2:][::-1]):
        if c == '0':
            if found_one:
                n[len(n)-i-1] = '1'
                break
            else:
                cnt_zeros += 1
        else:
            found_one = True
    n = int(''.join(n), 2)
    n &= ~((1 << i) - 1)
    right = 0
    for j in range(i - cnt_zeros - 1):
        right |= (1 << j)
    return n | right

print(bin(find_next2(list('0b011011001111100'))))

def find_previous2(n):
    cnt_ones = 0
    found_zero = False
    for i, c in enumerate(n[2:][::-1]):
        if c == '1':
            if found_zero:
                n[len(n)-i-1] = '0'
                break
            else:
                cnt_ones += 1
        else:
            found_zero = True
    n = int(''.join(n), 2)
    n &= ~((1 << i) - 1)
    right = 0
    for j in range(i - 1, i - cnt_ones - 2, -1):
        right |= (1 << j)
    return n | right

print(bin(find_previous2(list('0b10011110000011'))))