# Given an M x N matrix in which each row and column is sorted in ascending order, write a method to
# find an element.

# Time: O(M*log(N))
def find_element(m, el):
    for r, row in enumerate(m):
        c = binary_search(row, el, 0, len(row)-1)
        if c is not None:
            return r, c

def binary_search(a, el, lo, hi):
    if lo <= hi:
        mid = (lo + hi) // 2
        if el < a[mid]:
            return binary_search(a, el, lo, mid-1)
        elif el > a[mid]:
            return binary_search(a, el, mid+1, hi)
        else:
            return mid

if __name__ == "__main__":
    m = [[ 15 , 20 , 40 , 85  ],
         [ 20 , 35 , 80 , 95  ],
         [ 30 , 55 , 95 , 105 ],
         [ 40 , 80 , 100, 120 ]]
    el = 55
    print(find_element(m, el))
    el = 56
    print(find_element(m, el))


# Time: O(M+N)
def find_element(m, el):
    r = 0
    c = len(m) - 1
    while r < len(m) and c > 0:
        if el < m[r][c]:
            c -= 1
        elif el > m[r][c]:
            r += 1
        else:
            return r, c

if __name__ == "__main__":
    m = [[ 15 , 20 , 40 , 85  ],
         [ 20 , 35 , 80 , 95  ],
         [ 30 , 55 , 95 , 105 ],
         [ 40 , 80 , 100, 120 ]]
    el = 55
    print(find_element(m, el))
    el = 56
    print(find_element(m, el))


# Time: O(log(N+M))
def find_element(m, el):
    return _find_element(m, [0,0], [len(m)-1, len(m[0])-1], el)

def _find_element(m, origin, dest, x):
    if not inbounds(m, origin) or not inbounds(m, dest):
        return None
    if m[origin[0]][origin[1]] == x:
        return tuple(origin)
    elif not is_before(origin, dest):
        return None
    start = origin.copy()
    diagonal_distance = min(dest[0] - origin[0], dest[1] - origin[1])
    end = [start[0] + diagonal_distance, start[1] + diagonal_distance]
    p = [0, 0]
    while is_before(start, end):
        p = set_to_average(start, end)
        if x > m[p[0]][p[1]]:
            start[0] = p[0] + 1
            start[1] = p[1] + 1
        else:
            end[0] = p[0] - 1
            end[1] = p[1] - 1
    return partition_and_search(m, origin, dest, start, x)

def partition_and_search(m, origin, dest, pivot, x):
    lower_left_origin = [pivot[0], origin[1]]
    lower_left_dest = [dest[0], pivot[1]-1]
    upper_right_origin = [origin[0], pivot[1]]
    upper_right_dest = [pivot[0]-1, dest[1]]
    lower_left = _find_element(m, lower_left_origin, lower_left_dest, x)
    if lower_left is None:
        return _find_element(m, upper_right_origin, upper_right_dest, x)
    return lower_left

def set_to_average(origin, dest):
    return [(origin[0] + dest[0]) // 2, (origin[1] + dest[1]) // 2]

def is_before(origin, dest):
    return origin[0] <= dest[0] and origin[1] <= dest[1]

def inbounds(m, coordinate):
    r, c = coordinate
    return not (r < 0 or c < 0 or r >= len(m) or c >= len(m[0]))

if __name__ == "__main__":
    m = [[ 15 , 20 , 40 , 85  ],
         [ 20 , 35 , 80 , 95  ],
         [ 30 , 55 , 95 , 105 ],
         [ 40 , 80 , 100, 120 ]]
    el = 55
    print(find_element(m, el))
    el = 56
    print(find_element(m, el))


