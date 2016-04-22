# -*- coding: utf-8 -*-
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(nums, target, left, right):
            if left > right:
                if target > nums[right]:
                    return right+1
                if target < nums[right]:
                    return right-1

            mid = (left + right) / 2
            if nums[mid] > target:
                return search(nums, target, left, mid-1)
            elif nums[mid] < target:
                return search(nums, target, mid+1, right)
            elif nums[mid] == target:
                return mid
        if target < nums[0]:
            return 0
        return search(nums, target, 0, len(nums)-1)

print Solution().searchInsert([1], 4)
