# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
# 找出数列中连续的子数列,使得该子数列的和最大
# 当我们从头到尾遍历这个数组的时候，对于数组里的一个整数，它有几种选择呢？它只有两种选择：
# 1、加入之前的SubArray; 2. 自己另起一个SubArray。
# 如果之前SubArray的总体和大于0的话，我们认为其对后续结果是有贡献的。这种情况下我们选择加入之前的SubArray
# 如果之前SubArray的总体和为0或者小于0的话，我们认为其对后续结果是没有贡献，甚至是有害的（小于0时）。这种情况下我们选择以这个数字开始，另起一个SubArray。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_total = None
        total = None
        for item in nums:
            # 判断该值是否对当前子数列有利
            if total is None:
                total = item
            elif total > 0:
                total += item
            else:
                total = item
            # 记录最大值
            if max_total is None:
                max_total = total
            else:
                max_total = max(max_total, total)
        return max_total

s = [-2, 1, -2]
print Solution().maxSubArray(s)
