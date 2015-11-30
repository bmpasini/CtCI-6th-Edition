# A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def count_ways(n):
    return _count_ways(n, [None] * (n + 1))

def _count_ways(n, mem):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if mem[n] is None:
        mem[n] = _count_ways(n-3, mem) + _count_ways(n-2, mem) + _count_ways(n-1, mem)
    return mem[n]

def count_ways_bf(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways_bf(n-3) + count_ways_bf(n-2) + count_ways_bf(n-1)

def triple_step(n, step=0, cnt=0):
    if step >= n:
        return 1 + cnt
    if step + 1 <= n:
        cnt = triple_step(n, step+1, cnt)
    if step + 2 <= n:
        cnt = triple_step(n, step+2, cnt)
    if step + 3 <= n:
        cnt = triple_step(n, step+3, cnt)
    return cnt    

f = list()
for i in range(1, 11):
    f.append(count_ways(i))
print(f)

f = list()
for i in range(1, 11):
    f.append(count_ways_bf(i))
print(f)

f = list()
for i in range(1, 11):
    f.append(triple_step(i))
print(f)
