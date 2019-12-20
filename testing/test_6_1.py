from dataclasses import dataclass
from .test_utils.read_tsv import read_tsv

import problems._6_1.sol as solution


class test_schema:
    def __init__(self, number: int, string: str, desc: str = ""):
        self.number = number
        self.string = str(string)
        self.desc = desc


def test():
    test_data = read_tsv("6_1.tsv", test_schema)
    for test in test_data:
        assert solution.sol_int_to_str(test.number) == test.string, test.desc
        assert solution.sol_str_to_int(test.string) == test.number, test.desc
