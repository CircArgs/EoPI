from dataclasses import dataclass
from .test_utils.read_tsv import read_tsv

import problems._5_1.sol as solution


@dataclass
class test_schema:
    test: list
    sol: list
    desc: str = ""


def test():
    test_data = read_tsv("5_1.tsv", test_schema)
    for test in test_data:
        assert (
            solution.sol(test.test) == test.sol == solution.extra_space_sol(test.test)
        ), test.desc
