import random

from sol_8_1 import Stack


def test():
    for _ in range(1000):
        s = Stack()
        m = -float("inf")
        n = random.randint(0, 10000)
        temp = [None] * n
        for i in range(n):
            v = random.randint(-10000, 10000)
            if m < i:
                m = i
            s.push(i)
            assert s.max() == m
