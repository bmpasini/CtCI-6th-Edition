# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1, s2): # in this case spaces count and character comparison is case insensitive
    if len(s1) != len(s2):
        return False
    char_count = [0 for _ in range(256)] # assume ASCII extended
    for c in s1:
        char_count[ord(c)] += 1
    for c in s2:
        char_count[ord(c)] -= 1
        if char_count[ord(c)] < 0:
            return False
    return True