# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string a a b c c c c c a a a would become a2blc5a3. If the "compressed" string
# would not become smaller than the original string, your method should return the original string.

def str_compression(s):
    s_compressed = []
    last_c = s[0]
    cnt = 0
    for c in s[1:]:
        cnt += 1
        if last_c != c:
            s_compressed += [last_c, str(cnt)]
            cnt = 0
        last_c = c
    s_compressed += [last_c, str(cnt+1)]
    s_compressed = ''.join(s_compressed)
    if len(s_compressed) < len(s):
        return s_compressed
    else:
        return s


if __name__ == "__main__":
    import sys
    print(str_compression(sys.argv[1]))