# Given two strings s1 and s2, write code to check if s2
# is a rotation of s1 using only one call to isSubstring

def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = ''.join([s1, s1])
        if s2 in s1s1:
            return True
    return False


if __name__ == "__main__":
    import sys
    print(isRotation(sys.argv[1], sys.argv[2]))