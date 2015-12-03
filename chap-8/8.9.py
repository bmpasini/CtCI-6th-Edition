# Implement an algorithm to print all valid combinations of n pairs of parentheses.

# Time: O(n^2) (string concatation takes n time)
def parens(n):
    combinations = list()
    _parens(n, 0, 0, '', combinations)
    return combinations

def _parens(n, l, r, s, combinations):
    if len(s) == 2*n:
        combinations.append(s)
        return None
    if l < n:
        s_cp = s
        s_cp += '('
        _parens(n, l+1, r, s_cp, combinations)
    if r < l:
        s_cp = s
        s_cp += ')'
        _parens(n, l, r+1, s_cp, combinations)

if __name__ == "__main__":
    n = 4
    parens = parens(n)
    print(len(parens))
    print(parens)

# Using list of chars
# Time: O(n)
def parens(n):
    combinations = list()
    _parens(n, 0, 0, list(), combinations)
    return build_strings(combinations)

def _parens(n, l, r, s, combinations):
    if len(s) == 2*n:
        combinations.append(s)
        return None
    if l < n:
        s_cp = s.copy()
        s_cp.append('(')
        _parens(n, l+1, r, s_cp, combinations)
    if r < l:
        s_cp = s.copy()
        s_cp.append(')')
        _parens(n, l, r+1, s_cp, combinations)

def build_strings(chars_lists):
    str_list = list()
    for chars in chars_lists:
        str_list.append(''.join(chars))
    return str_list

if __name__ == "__main__":
    n = 4
    parens = parens(n)
    print(len(parens))
    print(parens)