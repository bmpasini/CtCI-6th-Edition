# Given an input file with four billion non-negative integers, provide an algorithm to generate
# an integer that is not contained in the file. Assume you have 1 GB of memory available for this task.
# FOLLOW UP
# What if you have only 10 MB of memory? Assume that all values are distinct an we now have no more than
# one billion non-negative integers.

# 2^31 different non-negative integers
# 1 GB = 2^33 bits
# create list of integers, each integer correspond to 64 numbers
# the list needs 2^(31 - 6) = 2^25 bytes to hold the information

def gen_integer(fname):
    bit_vector = [0] * (1 << 25)
    mark_bits(fname, bit_vector)
    return find_first_zero(bit_vector)

def find_first_zero(bit_vector):
    for i, integer in enumerate(bit_vector):
        for j in range(64):
            if ((integer >> j) & 1 == 0): # integer & (1 << i) == 0
                return 64 * i + j

def mark_bits(fname, bit_vector):
    with open(fname, 'r') as numbers:
        for n in numbers:
            try:
                mark_bit(int(n), bit_vector)
            except ValueError:
                pass

def mark_bit(number, bit_vector):
    list_position = number // 64
    bit_offset = number % 64
    bit_vector[list_position] |= (1 << bit_offset)

# FOLLOW UP

# (1)
# scan dataset once counting numbers within a range of size range_size
# store counts in range_count
# full ranges will have a count == range_size

# (2)
# scan dataset again looking for numbers, whose count != range_size and map them in a bit_vector

# (3)
# 10 MB of memory = 2^23 bits
# 2^30 distinct integers
# range_size < 2^23
# range_count < 2^23
# we can pick a range_size of 2^10 and a range_count of 2^13 elements

def gen_integer(fname):
    range_size = (1 << 10)
    range_counts = [0] * (1 << 13)
    count_ranges(fname, range_size, range_counts)
    start_of_range = find_range(range_counts, range_size)
    return find_integer(fname, start_of_range)

def find_integer(fname, start_of_range, range_size):
    bit_vector = mark_bits(fname, start_of_range, range_size)
    first_zero = find_first_zero(bit_vector)
    return start_of_range + first_zero

def find_first_zero(bit_vector):
    for i, integer in enumerate(bit_vector):
        for j in range(64):
            if (integer & (1 << j) == 0):
                return 64 * i + j
    
def mark_bits(fname, start_of_range, range_size):
    int_size = 64 # len(bin(sys.maxsize + 1)) - 2
    bit_vector = [0] * (range_size//int_size)
    with open(fname, 'r') as numbers:
        for n in numbers:
            if n >= start_of_range and n < start_of_range + range_size:
                mark_bit(n - start_of_range, bit_vector)
    return bit_vector

def mark_bit(number, bit_vector):
    bit_vector[number//64] |= (1 << (number % 64))

def find_range(range_counts, range_size):
    for i, count in enumerate(range_counts):
        if count != range_size:
            return i * range_size

def count_ranges(fname, range_size, range_counts):
    with open(fname, 'r') as numbers:
        for n in numbers:
            range_counts[n//range_size] += 1



