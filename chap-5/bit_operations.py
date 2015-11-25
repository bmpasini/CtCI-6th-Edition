def get_bit(num, i):
    return ((num & (1 << i)) != 0)

def set_bit(num, i):
    return num | (1 << i)

def clear_bit(num, i):
    return num & ~(1 << i)

def clear_bits_msb_through_i_inclusive(num, i):
    return num & ((1 << i) - 1)

def clear_bits_i_through_0_inclusive(num, i):
    return num & ~((1 << (i + 1)) - 1)

def update_bit(num, i, bit):
    return (num & ~(1 << i)) + (bit << i)