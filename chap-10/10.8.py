# You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have
# duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how
# would you print all duplicate elements in the array?

# 32000 <= 2^15
# 4kb = 2^15 bits = 32768 bits

def find_duplicates(a):
    bit_vector = [0] * 500 # 500 numbers of 64 bits each (32000 bits)
    for n in a:
        vector_position = (n-1) // 64
        offset = (n-1) % 64
        if (bit_vector[vector_position] & (1 << offset)) == 0:
            bit_vector[vector_position] |= (1 << offset)
        else:
            print(n)
            

if __name__ == "__main__":
    a = list()
    for i in range(32000):
        a.append(i)
    a[23322] = 22222
    a[222] = 7777
    find_duplicates(a)


class BitSet(object):

    def __init__(self, size):
        self.bit_vector = [0] * (size // 64 + 1)

    def get(self, n):
        vector_position = n // 64
        offset = n % 64
        return self.bit_vector[vector_position] & (1 << offset) != 0

    def set(self, n):
        vector_position = n // 64
        offset = n % 64
        self.bit_vector[vector_position] |= (1 << offset)

def print_duplicates(a):
    bs = BitSet(32000)
    for n in a:
        if bs.get(n-1):
            print(n)
        else:
            bs.set(n-1)


if __name__ == "__main__":
    a = list()
    for i in range(32000):
        a.append(i)
    a[23322] = 22222
    a[222] = 7777
    print_duplicates(a)