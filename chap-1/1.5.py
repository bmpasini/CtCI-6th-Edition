# Given two strings, write a function to check if they are one edit (or zero edits) away.

def check_edits(s1,s2):
    len_diff = len(s1) - len(s2)
    if abs(len_diff) > 1:
        return False
    elif abs(len_diff) == 1:
        if len_diff == -1:
            s1, s2 = s2, s1
        i = 0
        j = 0
        for _ in range(len(s2)):
            if s1[i] != s2[j] and i == j:
                i += 1
            elif s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                return False
    else:
        cnt = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] != s2[i]:
                cnt += 1
            if cnt > 1:
                return False
    return True
            

if __name__ == "__main__":
    import sys
    print(check_edits(sys.argv[1], sys.argv[2]))


