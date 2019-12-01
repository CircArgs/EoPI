import sys
import random


from .sol import parity, book_parity, dumb_brute_force


def test_parity():
    for i in range(100):
        n = random.randint(0, sys.maxsize)
        assert book_parity(n) == parity(n) == dumb_brute_force(n)
