# Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the
# binary representation. If the number cannot be represented accurately in binary with at most
# 32 characters, print "ERROR."

def binary_to_string(d):
    if d <= 0 or d >= 1:
        print("ERROR")
        return "ERROR"
    s = '.'
    b = 0.5
    while d > 0:
        if len(s) >= 32:
        # if len(s) >= 53: # there are 53 bits of precision available for a Python float
            print("ERROR")
            return s
        if d >= b:
            s += '1'
            d -= b
        else:
            s += '0'
        b /= 2.0
    return s

def binary_to_string2(d):
    if d <= 0 or d >= 1:
        print("ERROR")
        return "ERROR"
    s = '.'
    while d > 0:
        if len(s) >= 32:
        # if len(s) >= 53: # there are 53 bits of precision available for a Python float
            print("ERROR")
            return s
        r = 2 * d
        if r >= 1:
            s += '1'
            d = r - 1
        else:
            s += '0'
            d = r
    return s

if __name__ == "__main__":
    n = .72
    s = binary_to_string(n)
    print(s, len(s))
    total = 0.0
    b = 0.5
    s = s[1:]
    while len(s) != 0:
        if s[0] == '1':
            total += b
        s = s[1:]
        b /= 2.0
    print(total)

