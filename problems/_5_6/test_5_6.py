import random
import pytest


from sol_5_6 import sol, book_sol


@pytest.fixture
def random_list():
    return [random.randint(0, 1000) for i in range(random.randint(0, 1000))]


def test(random_list):
    for i in range(10000):
        assert sol(random_list) == book_sol(random_list)
