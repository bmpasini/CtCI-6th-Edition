# Write a method to sort an array of strings so that all the anagrams are next to each
# other.

# Time: O(l * n*log(n) + l*log(l) + l), l = length of array, n = chars in array
def group_anagrams(a):
    map_anagrams = dict()
    for s in a:
        map_anagrams[s] = ''.join(sorted(s))
    return [ k for k,v in sorted(map_anagrams.items(), key=lambda x: x[1]) ]

if __name__ == "__main__":
    a = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cba']
    print(group_anagrams(a))

# Time: O(l * n*log(n) + l), l = length of array, n = chars in array
def group_anagrams(a):
    map_anagrams = dict()
    for s in a:
        anagram = ''.join(sorted(s))
        if anagram in map_anagrams.keys():
            map_anagrams[anagram].append(s)
        else:
            map_anagrams[anagram] = [s]
    result = list()
    for v in map_anagrams.values():
        result += v
    return result

if __name__ == "__main__":
    a = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cba']
    print(group_anagrams(a))

# Using comparable protocol (how?)
class StrAnagram(str):

    def __lt__(self, other):
        sorted(self) < sorted(other)

    def __gt__(self, other):
        sorted(self) > sorted(other)

    def __eq__(self, other):
        sorted(self) == sorted(other)

    def __le__(self, other):
        sorted(self) <= sorted(other)

    def __ge__(self, other):
        sorted(self) >= sorted(other)

    def __ne__(self, other):
        sorted(self) != sorted(other)

def group_anagrams(a):
    a_sortable = list()
    for s in a:
        a_sortable.append(StrAnagram(s))
    return sorted(a_sortable)

if __name__ == "__main__":
    a = ['bbb', 'abc', 'ccc', 'bca', 'aaa', 'cba']
    print(group_anagrams(a))