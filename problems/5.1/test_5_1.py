import pytest
import random

from sol_5_1 import sol, extra_space_sol


@pytest.fixture
def random_list():
    length = random.randint(0, 100)
    return [random.randint(0, 100) for _ in range(length)]


def test(random_list):
    assert sorted(random_list) == extra_space_sol(random_list) == sol(random_list)

