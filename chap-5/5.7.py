# Write a program to swap odd and even bits in an integer with as few instructions as possible
# (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and soon).

# assuming 32-bit integers
def pairwise_swap(n):
    odd_mask  = int("0xaaaaaaaa", 16) # ...1010
    even_mask = int("0x55555555", 16) # ...0101
    # return (((n & odd_mask) >> 1) | ((n & even_mask) << 1))
    return ((((n & odd_mask) % "0x100000000") >> 1) | ((n & even_mask) << 1)) # logical right shift

if __name__ == "__main__":
    n = 3698
    print(bin(n))
    print(bin(pairwise_swap(n)))
