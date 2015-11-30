# Write a recursive function to multiply two numbers without using the * operator. You can use
# addition, subtraction, and bit shifting, but you should minimize the number of those operations.

# Time complexity: O(log(s))
# Space complexity: O(log(s))
# Where s is the smallest number
def recursive_multiply(a, b):
    if a >= b:
        return _recursive_multiply(a, b, 0)
    else:
        return _recursive_multiply(b, a, 0)

def _recursive_multiply(a, b, i):
    if b == 0:
        return 0
    total = _recursive_multiply(a, b >> 1, i + 1)
    if (b & 1) == 1:
        total += (a << i)
    return total


def recursive_multiply2(a, b):
    if a >= b:
        return _recursive_multiply2(a, b)
    else:
        return _recursive_multiply2(b, a)

def _recursive_multiply2(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a
    half = _recursive_multiply2(a, b >> 1)
    if b % 2 == 0:
        return half << 1
    else:
        return a + (half << 1)

if __name__ == "__main__":
    # my method
    print(recursive_multiply(15, 0))
    print(recursive_multiply(15, 15))
    print(recursive_multiply(0, 15))
    print(recursive_multiply(0, 0))
    print(recursive_multiply(7, 7))
    print(recursive_multiply(2, 7))
    print(recursive_multiply(14, 22))
    # bok method
    print(recursive_multiply2(15, 0))
    print(recursive_multiply2(15, 15))
    print(recursive_multiply2(0, 15))
    print(recursive_multiply2(0, 0))
    print(recursive_multiply2(7, 7))
    print(recursive_multiply2(2, 7))
    print(recursive_multiply2(14, 22))