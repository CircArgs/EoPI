cache = {}


def cache_checker(n: int) -> int:
    v = cache.pop(n, None)
    if v != None:
        cache[v] = v
        return v
    else:
        v = parity(n)
    cache[n] = v
    return v


# this is barely slower
# def ones(n):
#     return 2 ** n.bit_length() - 1
# than this:
def ones(n: int) -> int:
    if not n:
        return 1
    return int("1" * n.bit_length(), 2)


def _parity(n: int) -> int:
    bl = n.bit_length()
    if bl < 2:
        return n
    if bl % 2:
        return ((n & 1) + cache_checker(n >> 1)) % 2
    else:
        temp = n >> (bl // 2)
        return cache_checker((ones(temp) & n) ^ temp)


def parity(n:int)->int:
    return _parity(abs(n))