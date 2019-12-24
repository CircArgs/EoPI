from dataclasses import dataclass
from typing import List
from .test_utils.read_tsv import read_tsv

import problems._10_1.sol as solution


@dataclass
class test_schema:
    test: List[List[int]]
    sol: List[int]
    desc: str


def test():
    test_data = read_tsv("10_1.tsv", test_schema)
    for test_number, test in enumerate(test_data):
        assert (
            solution.sol(*test.test) == test.sol
        ), f"test_number: {test_number}: {test.test}; {test.sol}; {test.desc}"
