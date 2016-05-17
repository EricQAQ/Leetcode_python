# -*- coding: utf-8 -*-
"""
Say you have an array for which the i^th element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""
# 给予一个数列,表示某股票n天的股价, 求最大利润
# 关键是记录最低股价和最大利润,遍历即可


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = None
        for item in prices[1:]:
            min_price = min(min_price, item)
            if not max_profit:
                max_profit = item - min_price
            else:
                max_profit = max(max_profit, item-min_price)

        return max_profit
