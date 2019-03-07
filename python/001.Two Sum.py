# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        process = {}
        for pos, num in enumerate(nums):
            if target - num in process:
                return [pos, process[target-num]]
            process[num] = pos

if __name__ == '__main__':
    s = Solution()
    tmp = s.twoSum([2, 7, 11, 15], 9)
    tmp.sort()
    assert tmp == [0, 1]
