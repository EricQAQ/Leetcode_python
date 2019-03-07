# -*- coding: utf-8 -*-
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
# 看到复杂度要求是O(log n), 想到二分法
# 大体思路是 用二分法找到对应值的位置,然后分别向左右两边循环扩展


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(nums, target, left, right):
            if left > right:
                return [-1, -1]
            mid = (left + right) / 2
            if nums[mid] > target:
                return search(nums, target, left, mid-1)
            elif nums[mid] < target:
                return search(nums, target, mid+1, right)
            elif nums[mid] == target:
                tmp = mid
                _start = _end = None
                while nums[mid] == target:
                    if mid == 0:
                        _start = 0
                        break
                    mid -= 1
                if _start is not None:
                    start = _start
                else:
                    start = mid+1

                while nums[tmp] == target:
                    if tmp == len(nums)-1:
                        _end = tmp
                        break
                    tmp += 1
                if _end is not None:
                    end = _end
                else:
                    end = tmp-1
                return [start, end]

        if not nums:
            return [-1, -1]

        return search(nums, target, 0, len(nums)-1)
