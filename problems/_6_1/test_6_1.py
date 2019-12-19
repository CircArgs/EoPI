import random
import pytest


from sol_6_1 import (
    sol_int_to_str,
    sol_str_to_int,
    book_sol_str_to_int,
    book_sol_int_to_str,
)


@pytest.fixture
def random_number():
    return random.randint(-10e20, 10e20)


def test_strs(random_number):
    for i in range(10000):
        assert sol_int_to_str(random_number) == book_sol_int_to_str(random_number)


def test_ints(random_number):
    for i in range(10000):
        assert sol_str_to_int(str(random_number)) == book_sol_str_to_int(
            str(random_number)
        )
