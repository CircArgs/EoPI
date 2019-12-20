from dataclasses import dataclass
from .test_utils.read_tsv import read_tsv

import problems._4_1.sol as solution


@dataclass
class test_schema:
    test: int
    sol: int
    desc: str = ""


def test_parity():
    test_data = read_tsv(
        "/home/nick/Documents/EoPI/test_problems/test_data/4_1.tsv", test_schema
    )
    for test in test_data:
        assert solution.sol(test.test) == test.sol, test.desc
