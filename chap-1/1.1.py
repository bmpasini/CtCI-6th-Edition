# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique_with_ds(s): # n in space and time
    if len(s) > 256: # assume ASCII extended
        return False
    bitmap = [False for _ in range(256)]
    for c in s:
        if bitmap[ord(c)]:
            return False
        else:
            bitmap[ord(c)] = True
    return True

def is_unique(s):
    s.sort() # n*log(n) / #[].sort() is in-place, whereas sorted() creates a copy of the list
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True
