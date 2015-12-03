# Write a method to compute all permutations of a string whose characters are not necessarily unique.
# The list of permutations should not have duplicates.

# Time complexity: O(n!)
# Space complexity: O(n!)

def perm_dup(s):
    if s is None:
        return None
    if len(s) < 2:
        return s
    s = list(s)
    permutations = list()
    char_freq = char_counts(s)
    results = list()
    _perm_dup(list(), len(s), char_freq, permutations)
    for perm in permutations:
        results.append(''.join(perm))
    return results

def char_counts(s):
    counts = dict()
    for c in s:
        try:
            counts[c] += 1
        except KeyError:
            counts[c] = 1
    return counts

def _perm_dup(s, remaining, char_freq, permutations):
    if remaining == 0:
        permutations.append(s)
        return None
    for c in char_freq.keys():
        if char_freq[c] > 0:
            s_cp = s.copy()
            s_cp.append(c)
            char_freq[c] -= 1
            _perm_dup(s_cp, remaining-1, char_freq, permutations)
            char_freq[c] += 1

if __name__ == "__main__":
    s = 'abcc'
    permutations = perm_dup(s)
    print(len(permutations))
    print(permutations)
    s = 'abcd'
    permutations = perm_dup(s)
    print(len(permutations))
    print(permutations)


