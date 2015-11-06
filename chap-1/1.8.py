# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0

# space complexity O(k), where k is the number os zeros in matrix
# time complexity O(N^2)
def set_zero(m, M, N):
    rows = set()
    cols = set()
    for row in range(M):
        for col in range(N):
            if m[row][col] == 0:
                rows.add(row)
                cols.add(col)
    for row in rows:
        m[row] = [ 0 for _ in range(N) ]
    for col in cols:
        for row in range(M):
            m[row][col] = 0
    for row in range(M):
        print(m[row])

# space complexity O(1)
# time complexity O(N^2), it takes a few more iterations though
def set_zero(m, M, N):
    for row in range(M):
        for col in range(N):
            if m[row][col] == 0:
                m[row][0] = 0
                m[0][col] = 0
    for row in range(N):
        if m[row][0] == 0:
            m[row] = [ 0 for _ in range(N) ]
    for col in range(M):
        if m[0][col] == 0:
            for row in range(M):
                m[row][col] = 0
    for row in range(M):
        print(m[row])

if __name__ == "__main__":
    m = [[1 ,2 ,3 ,4 ],
         [5 ,6 ,7 ,8 ],
         [9 ,0 ,11,12],
         [13,14,15,16]]
    set_zero(m, 4, 4)