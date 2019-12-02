"""
EoPI pg 46

This problem is concerned with the problem of optimally buying and selling a stock once,
as described on Page 2. As an example, consider the following sequence of stock prices:
<310,315,275,295,260,270,290,230,255,250>. The maximum profit that can be made with one buy
and one sell is 30-buy at 260 and sell at 290. Note that 250 is not the lowest price, nor 290 the
highest price.

ex. sol([310,315,275,295,260,270,290,230,255,250]) -> 30
"""


from typing import List


def sol(prices: List[int]) -> int:
    """
    takes a list of stock prices and determines the highest profit given buying one day and selling at a later day one single time
    Time complexity O(n)
    Space complexity: O(1)
    Args:
        prices: list of stock prices per day

    Returns:
        maximum profit int
    """
    # we will iterate through the array and set the minimum price we've seen yet
    # as well as the maximum difference seen yet
    min_seen = float("inf")
    max_diff = 0
    for v in prices:
        if v < min_seen:
            min_seen = v
        diff = v - min_seen
        if diff > max_diff:
            max_diff = diff
    return max_diff


###################for testing########################
def book_sol(prices: List[int]) -> int:
    min_price_so_far, max_profit = float("inf"), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit
