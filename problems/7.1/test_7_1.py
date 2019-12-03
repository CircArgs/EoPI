import random
from sol_7_1 import sol, Linked_List


def random_list():
    return [random.randint(-1000, 1000) for _ in range(0, 1000)]


def test():
    for _ in range(100):
        rl1 = sorted(random_list())
        rl2 = sorted(random_list())
        test_list = sorted(rl1 + rl2)
        rll1 = Linked_List.from_list(rl1)
        rll2 = Linked_List.from_list(rl2)
        assert test_list == list(map(lambda x: x.val, sol(rll1, rll2).iter()))
