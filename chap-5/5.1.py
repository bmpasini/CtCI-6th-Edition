# You are given two 32-bit numbers, Nand M, andtwo bit positions, land j. Write
# a method to insert M into Nsuch that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is,
# if M = 10011, you canassumethat there areat least 5 bits between j and i. You
# would not,forexample, have j = 3 and i = 2,because M could notfully fit between
# bit 3 and bit 2.

def insertion(N, M, i, j):
    return (M << i) | (N & ~(((1 << (j - i + 2)) - 1) << i))

def insertion2(N, M, i, j):
    return (M << i) | (N & ((~0 << (j + 1)) | ((1 << i) - 1)))

if __name__ == "__main__":
    N = int('10000000000', 2)
    M = int('10011', 2)
    i = 2
    j = 6
    print(bin(insertion(N, M, i, j)))
    print(bin(insertion2(N, M, i, j)))