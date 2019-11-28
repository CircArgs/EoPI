import sys
import random

from sol import parity, cache


def dumb_brute_force(n):
    """a solution so dumb it can't be wrong"""
    n = bin(abs(n))[2:]
    return sum(int(i) for i in n) % 2


def d_parity(x):
    x = abs(x)
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drops the -lowest set bit of
    return result


def test_parity():
    for i in range(100):
        n = random.randint(0, sys.maxsize)
        assert d_parity(n) == parity(n)
