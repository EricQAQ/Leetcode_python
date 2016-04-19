# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
# 求a+b+c=0 可以转化为a+b=-c


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        _list = []
        nums.sort()

        for pos, item in enumerate(nums):
            start = pos + 1
            end = len(nums) - 1

            while start < end:
                if nums[start] + item + nums[end] == 0:
                    if [item, nums[start], nums[end]] not in _list:
                        _list.append([item, nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif nums[start] + item + nums[end] < 0:
                    start += 1
                elif nums[start] + item + nums[end] > 0:
                    end -= 1
        return _list
