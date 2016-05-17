# -*- coding: utf-8 -*-
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _list = [0]
        _list.extend([1 for i in range(len(nums))])
        max_len = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] >= nums[j] and _list[j] + 1 > _list[i]:
                    _list[i] = _list[j] + 1
            if _list[i] > max_len:
                max_len = _list[i]
        return max_len

print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

