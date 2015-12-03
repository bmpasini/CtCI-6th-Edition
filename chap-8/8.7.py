# Write a method to compute all permutations of a string of unique characters.

s = 'abcde'

# Time complexity: O(n!)
# Space complexity: O(n!)

def permutations_without_dups(s):
    if s is None:
        return None
    if len(s) == 1:
        return s
    s = list(s)
    permutations = _permutations_without_dups(s)
    result = list()
    for p in permutations:
        result.append(''.join(p))
    return result

def _permutations_without_dups(s):
    if len(s) == 2:
        return [ s, s[::-1] ]
    permutations = list()
    for c in s:
        s_cp = s.copy()
        s_cp.remove(c)
        for permutation in _permutations_without_dups(s_cp):
            permutations.append([ c ] + permutation)
    return permutations

if __name__ == "__main__":
    permutations = permutations_without_dups(s)
    print(len(permutations))
    print(permutations)

# Time complexity: O(n!)
# Space complexity: O(n!)

def permutations_without_dups2(s):
    if s is None:
        return None
    s = list(s)
    permutations = _permutations_without_dups2(s)
    result = list()
    for p in permutations:
        result.append(''.join(p))
    return result

def _permutations_without_dups2(s):
    if len(s) == 1:
        return [ s ]
    permutations = list()
    for c in s:
        s_cp = s.copy()
        s_cp.remove(c)
        for i, permutation in enumerate(_permutations_without_dups2(s_cp)):
            permutation_cp = permutation.copy()
            permutation_cp.insert(i, c)
            permutations.append(permutation_cp)

    return permutations

if __name__ == "__main__":
    permutations = permutations_without_dups2(s)
    print(len(permutations))
    print(permutations)