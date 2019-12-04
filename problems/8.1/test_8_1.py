import random

from sol_8_1 import Stack


def test():
    for _ in range(1000):
        s = Stack()
        m = -float("inf")
        for i in range(random.randint(0, 10000)):
            ri = random.randint(-10000, 10000)
            s.push(ri)
            if ri > m:
                m = ri
            if random.randint(0, 1) and len(s) > 1:
                s.pop()
            assert s.max() == m
