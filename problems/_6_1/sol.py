"""
EoPI pg 68

A string is a sequence of characters. A string may encode an integer e.g., "123" encodes 123. In
this problem, you are to implement methods that take a string representing an integer and return
the corresponding integer, and vice versa. Your code should handle negative integers. You cannot
use library functions like `int` in Python.

Example:
sol_int_to_str(-10)->'-10'
sol_str_to_int('-10')-> -10
"""


def sol_int_to_str(n: int) -> str:
    """convert an integer to a string
    Args:
        n int to convert

    Returns:
        n as string
    """
    if n == 0:
        return "0"
    ret = ""
    is_negative = n < 0
    n = abs(n)
    while True:
        if n == 0:
            break
        ret += str(n % 10)
        n //= 10
    return ("-" if is_negative else "") + ret[::-1]


def sol_str_to_int(n: str) -> int:
    """convert a string to an integer
    Args:
        n str to convert

    Returns:
        n as integer
    """
    n = list(n)
    is_negative = n[0] == "-"
    if is_negative:
        n = n[1:]
    n = sum(
        map(
            lambda t: string.digits.index(t[0]) * (10 ** t[1]),
            zip(n, range(len(n) - 1, -1, -1)),
        )
    )
    return (-1 if is_negative else 1) * n


#####################for testing########################

import functools
import string


def book_sol_str_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == "-" :],
        0,
    ) * (-1 if s[0] == "-" else 1)


def book_sol_int_to_str(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord("0") + x % 10))
        x //= 10
        if x == 0:
            break
    # Adds the negative sign back if is_negative
    return ("-" if is_negative else "") + "".join(reversed(s))
