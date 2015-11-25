# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of 1s you could create.

def flip_bit_to_win(n):
    n = bin(n)
    a = 0
    b = 0
    _max = 1
    for i in range(2, len(n) + 1):
        if i < len(n) and n[i] == '1':
            b += 1
        else:
            if a + b + 1 > _max:
                _max = a + b + 1
            a = b
            b = 0
    return _max

if __name__ == "__main__":
    print(flip_bit_to_win(1775)) # => 8
    print(flip_bit_to_win(221)) # => 6
    print(flip_bit_to_win(114409)) # => 9
