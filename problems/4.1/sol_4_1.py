"""EoPI pg 24
The parity of a binary word is 1
if the number of 1s in the word is odd; otherwise, it is 0.
For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.
How would you compute the parity of a very large number of 64-bit words?
Hint: Use a lookup table, but don't use
2^64
entries!
"""

# we use a dictionary (hash table) as a cache. we cache words (bit sequences) and subwords we haven't seen before.
# the cache could be modified to use a least recently used (LRU) cache with a max size
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


def parity(n: int) -> int:
    return _parity(abs(n))


#######FOR TESTING#######
def dumb_brute_force(n):
    """a solution so dumb it can't be wrong"""
    n = bin(abs(n))[2:]
    return sum(int(i) for i in n) % 2


def book_parity(x):
    """book's simple solution"""
    x = abs(x)
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drops the -lowest set bit of
    return result
