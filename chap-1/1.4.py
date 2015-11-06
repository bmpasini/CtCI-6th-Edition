# Given a string wrtie a function to check if it is a permutation of a palindrome

# 3 passes
def is_permutation_of_palindrome(s):
    char_count = { c : 0 for c in s }
    for c in s:
        char_count[c] += 1
    odd_cnt = 0
    for c in char_count:
        if not c.isalnum(): # assuming that .isalnum() is O(1) for 1 character
            continue
        if char_count[c] % 2 == 1:
            odd_cnt += 1
        if odd_cnt > 1:
            return False
    return True

# 2 passes
def is_permutation_of_palindrome(s):
    char_count = {}
    for c in s:
        try:
            char_count[c] += 1
        except KeyError:
            char_count[c] = 1
    odd_cnt = 0
    for c in char_count:
        if not c.isalnum():
            continue
        if char_count[c] % 2 == 1:
            odd_cnt += 1
        if odd_cnt > 1:
            return False
    return True

# 1 pass
def is_permutation_of_palindrome(s):
    char_count = {}
    odd_cnt = 0
    for c in s:
        if not c.isalnum():
            continue
        try:
            char_count[c] += 1
        except KeyError:
            char_count[c] = 1
        if char_count[c] % 2 == 1:
            odd_cnt += 1
        else:
            odd_cnt -=1
    return odd_cnt < 2
