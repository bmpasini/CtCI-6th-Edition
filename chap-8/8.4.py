# Write a method to return all subsets of a set.

# Using combinatorics

def power_set_bin(s):
    all_subsets = list()
    for i in range(1 << len(s)):
        all_subsets.append(convert_int_to_set(s, i))
    return all_subsets

def convert_int_to_set(s, i):
    subset = list()
    j = len(s)-1
    while i != 0:
        if (i & 1) == 1:
            subset.append(s[j])
        j -= 1
        i >>= 1
    return subset

# Using recursion

def power_set(s):
    return _power_set(s, 0)

def _power_set(s, i):
    all_subsets = list()
    if i == len(s):
        all_subsets.append(list())
    else:
        all_subsets = _power_set(s, i+1)
        el = s[i]
        more_subsets = list()
        for subset in all_subsets:
            new_subset = list()
            new_subset += subset
            new_subset.append(el)
            more_subsets.append(new_subset)
        all_subsets += more_subsets
    return all_subsets

# In both cases:
# Time complexity: O(2^n)
# Space complexity: O(2^n)

if __name__ == "__main__":
    s = [ 1, 2, 3 ]
    print(power_set(s))
    print(power_set_bin(s))