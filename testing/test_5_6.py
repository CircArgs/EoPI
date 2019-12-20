from dataclasses import dataclass
import math
from typing import List
from .test_utils.read_tsv import read_tsv

import problems._5_6.sol as solution


@dataclass
class test_schema:
    test: List[float]
    sol: float
    desc: str = ""


def test():
    test_data = read_tsv("5_6.tsv", test_schema)
    for test in test_data:
        assert math.isclose(solution.sol(test.test), test.sol, abs_tol=10e-6), test.desc
