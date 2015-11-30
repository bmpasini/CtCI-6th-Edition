# Iterative solution
# Time: O(n)
# Space: O(1)
def fib(n):
    if n < 2:
        return n
    a = 0
    b = 1
    for i in range(2, n):
        a, b = b, a + b
    return a + b

# Bottom-up dynamic programming
# Time: O(n)
# Space: O(n)
def fib_bu(n):
    if n < 2:
        return n
    mem = n * [None]
    mem[0] = 0
    mem[1] = 1
    for i in range(2, n):
        mem[i] = mem[i-1] + mem[i-2]
    return mem[n-1] + mem[n-2]

# Top-down dynamic programming or Memoization
# Time: O(n)
# Space: O(n)
def fib_mem(n):
    return _fib_mem(n , (n + 1) * [None])

def _fib_mem(n, mem):
    if n < 2:
        return n
    if mem[n] is None:
        mem[n] = _fib_mem(n-1, mem) + _fib_mem(n-2, mem)
    return mem[n]

# Careless recursive approach
# Time: O(2^n)
# Space: O(n)
def fib_bad(n):
    if n < 2:
        return n
    return fib_bad(n-1) + fib_bad(n-2)

f = list()
for i in range(32):
    f.append(fib(i))
print(f)

f = list()
for i in range(32):
    f.append(fib_bu(i))
print(f)

f = list()
for i in range(32):
    f.append(fib_mem(i))
print(f)

f = list()
for i in range(32):
    f.append(fib_bad(i))
print(f)
