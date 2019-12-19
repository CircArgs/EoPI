"""EoPI pg 24
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
For example, the parity of 1011 is 1, and the parity of 10001000 is 0. 
Parity checks are used to detect single bit errors in data storage and communication. 
It is fairly straightforward to write code that computes the parity of a single 64-bit word.
How would you compute the parity of a very large number of 64-bit words?
Hint: Use a lookup table, but don't use 2^64 entries!
"""


from collections import defaultdict
from typing import Callable


class Cache(defaultdict):
    """
    cache class classes elements it has not yet seen
    """

    def __init__(self, func: Callable):
        super().__init__()
        self.func = func

    # If dict lookup fails this will be called
    def __missing__(self, key: int) -> int:
        # Insert the parity of the key into the cache dict and return it
        value = self.func(key)
        self[key] = value
        return value

    def __call__(self, key: int) -> int:
        return self.__getitem__(key)


# this is barely slower
# def get_ones(n: int) -> int:
#     '''generate largest number of bit length n'''
#     return 2 ** n - 1


# than this:
# def get_ones(n: int) -> int:
#     if not n:
#         return 1
#     return int("1" * n, 2)
# but uses less memory in avoiding strings

# and this one is fastest of the three


def get_ones(n: int) -> int:
    """generate largest number of bit length n

    ex. ones(5) -> 7; bin(7) = 0b111
    
    Args:
        n: integer to get int corresponding to 1's of same bit length
    """

    return (1 << n) - 1


ones = Cache(get_ones)


def _parity(n: int) -> int:
    """generate largest number of bit length n
    
    Args:
        n: integer to get parity of
    
    Returns:
        int 0 or 1 for parity
    """
    bl = n.bit_length()
    if bl < 2:
        return n
    if bl % 2:
        return ((n & 1) + cache[n >> 1]) % 2
    else:
        temp = n >> (bl // 2)
        return cache[(ones(bl // 2) & n) ^ temp]


# we create a hashtable based cache by extending defaultdict. we cache words (bit sequences) and subwords we haven't seen before.
# the cache could be modified to use a least recently used (LRU) cache with a max size
cache = Cache(_parity)


def sol(n: int) -> int:
    return _parity(abs(n))


#######FOR TESTING#######
# def dumb_brute_force(n: int) -> int:
#     """a solution so dumb it can't be wrong"""
#     n = bin(abs(n))[2:]
#     return sum(int(i) for i in n) % 2


# def book_parity(x: int) -> int:
#     """book's simple solution"""
#     x = abs(x)
#     result = 0
#     while x:
#         result ^= 1
#         x &= x - 1  # Drops the -lowest set bit of
#     return result


# warm start caches
for i in range(32):
    cache[i]
    ones[i]
