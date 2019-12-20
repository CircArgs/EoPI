from dataclasses import dataclass
from .test_utils.read_tsv import read_tsv

import problems._4_1.sol as solution


@dataclass
class test_schema:
    test: int
    sol: int
    desc: str = ""


def test():
    test_data = read_tsv("4_1.tsv", test_schema)
    for test in test_data:
        assert solution.sol(test.test) == test.sol, test.desc
