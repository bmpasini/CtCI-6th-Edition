# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end of the string to hold the
# additional characters, and that you are given the "true" length of the string.
# Do it in place.

def URLify(s, length):
    new_length = length
    for i in range(len(s)):
        if s[i] == ' ':
            s.append(' ')
            s.append(' ')
            new_length += 2
    for i in range(length-1, -1, -1):
        if s[i] == ' ':
            s[new_length-1] = '0'
            s[new_length-2] = '2'
            s[new_length-3] = '%'
            new_length -= 3
        else:
            s[new_length-1] = s[i]
            new_length -= 1