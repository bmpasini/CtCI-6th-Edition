# Write a function to determine the number of bits required to convert integer A to integer B.

def conversion(a, b):
    cnt = 0
    while a != 0 or b != 0:
        if a % 2 != b % 2:
            cnt += 1
        a >>= 1
        b >>= 1
    return cnt

def conversion2(a, b):
    x = a ^ b
    cnt = 0
    while x != 0:
        cnt += (x % 2)
        x >>= 1
    return cnt

def conversion3(a, b):
    x = a ^ b
    cnt = 0
    while x != 0:
        cnt += 1
        x &= x - 1
    return cnt

if __name__ == "__main__":
    a = 339
    b = 427
    print(bin(a))
    print(bin(b))
    print(conversion(a, b))
    print(conversion2(a, b))
    print(conversion3(a, b))