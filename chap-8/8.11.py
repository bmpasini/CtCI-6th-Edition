# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

def coins(n):
    ways = _coins(n, 0, list(), {1:0,5:0,10:0,25:0})
    print(ways)
    return len(ways)

def _coins(n, total, ways, coins_used):
    if total == n:
        for way in ways:
            if way == coins_used:
                return None
        ways.append(coins_used)
    elif total >= n:
        return None
    if total % 1 == 0:
        coins_used_cp = coins_used.copy()
        coins_used_cp[1] += 1
        _coins(n, total+1, ways, coins_used_cp)
    if total % 5 == 0:
        coins_used_cp = coins_used.copy()
        coins_used_cp[5] += 1
        _coins(n, total+5, ways, coins_used_cp)
    if total % 10 == 0:
        coins_used_cp = coins_used.copy()
        coins_used_cp[10] += 1
        _coins(n, total+10, ways, coins_used_cp)
    if total % 25 == 0:
        coins_used_cp = coins_used.copy()
        coins_used_cp[25] += 1
        _coins(n, total+25, ways, coins_used_cp)
    return ways


def make_change(n):
    coins = [ 25, 10, 5, 1 ]
    return _make_change(n, coins, 0)

def _make_change(n, coins, i):
    if i >= len(coins) - 1:
        return 1
    ways = 0
    possibilities = n // coins[i]
    for j in range(possibilities + 1):
        ways += _make_change(n - j * coins[i], coins, i + 1)
    return ways


def make_change_improved(n):
    coins = [ 25, 10, 5, 1 ]
    ways_cache = [ [ None for _ in range(len(coins)) ] for _ in range(n+1) ]
    return _make_change_improved(n, coins, 0, ways_cache)

def _make_change_improved(n, coins, i, ways_cache):
    if ways_cache[n][i] is not None:
        return ways_cache[n][i]
    if i >= len(coins) - 1:
        return 1
    ways = 0
    possibilities = n // coins[i]
    for j in range(possibilities + 1):
        ways += _make_change_improved(n - j * coins[i], coins, i + 1, ways_cache)
    ways_cache[n][i] = ways
    return ways

if __name__ == "__main__":
    n = 75
    print(make_change_improved(n))
    print(make_change(n))
    print(coins(n))


