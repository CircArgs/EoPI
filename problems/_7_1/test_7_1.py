import random

from utils_7_1 import Linked_List
from sol_7_1 import sol


def random_list():
    return [random.randint(-1000, 1000) for _ in range(0, 1000)]


def test():
    for i in range(100):
        rl1 = sorted(random_list())
        rl2 = sorted(random_list())
        test_list = sorted(rl1 + rl2)
        rll1 = Linked_List.from_list(rl1)
        rll2 = Linked_List.from_list(rl2)

        fin = sol(rll1, rll2)
        assert test_list == list(map(lambda x: x.val, fin.iter()))
