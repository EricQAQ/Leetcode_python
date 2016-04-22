# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
# 看到已排好序的数组,想到二分法搜索.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def _search(nums, target, left, right):
            if left > right:
                return -1
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            mid = (left + right) / 2
            if nums[left] < nums[right]:    # 正常顺序
                if nums[mid] > target:
                    return _search(nums, target, left, mid-1)
                elif nums[mid] < target:
                    return _search(nums, target, mid+1, right)
                elif nums[mid] == target:
                    return mid
            elif nums[mid] > nums[left]:    # left ~ mid 为升序
                if nums[left] <= target <= nums[mid]:
                    return _search(nums, target, left, mid)
                else:
                    return _search(nums, target, mid+1, right)
            else:   # left ~ right 为升序
                if nums[mid] <= target <= nums[right]:
                    return _search(nums, target, mid, right)
                else:
                    return _search(nums, target, left, mid-1)

        return _search(nums, target, 0, len(nums)-1)
