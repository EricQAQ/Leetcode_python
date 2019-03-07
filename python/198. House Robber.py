# -*- coding: utf-8 -*-
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight
without alerting the police.
"""
# 在数组里面找一个序列， 序列里面的每一个元素都不能相邻，然后求其最大和


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        rob_ = 0
        not_rob = 0
        for item in nums:
            rob_ = item + not_rob   # 抢这间房子, 等效于这间房子的价值+不抢上间房子
            not_rob = max_value     # 不抢这间房子
            max_value = max(rob_, not_rob)
        return max_value
