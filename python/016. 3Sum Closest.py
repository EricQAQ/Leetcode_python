# -*- coding: utf-8 -*-
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []

        nums.sort()
        min_value = None

        for pos, item in enumerate(nums):
            start = pos + 1
            end = len(nums) - 1

            while start < end:
                tmp = item + nums[start] + nums[end]
                if min_value is None or abs(tmp - target) < abs(min_value - target):
                    min_value = tmp
                if tmp <= target:
                    start += 1
                else:
                    end -= 1
        return min_value

