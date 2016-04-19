# -*- coding: utf-8 -*-
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
# V = max[ (a2 - a1) * min(height[a2], height[a1]) ]
# 使用双指针,两头遍历
# 如果左值(v_L) < 右值(v_R), 左指针右移, 因为不管右边取数组中在左指针的右边的任何值v, 都不会比当前值大:
# 1. 如果v < v_L: min(height[a2], height[a1])=v, 体积V' < V
# 2. 如果v > v_L: min(height[a2], height[a1])=v_L和之前保持不变, 但是(a2 - a1)却减少了, 体积V' < V
# 同理, 如果左值 > 右值, 右指针左移

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_ = 0

        while start < end:
            if height[start] < height[end]:
                tmp = (end-start) * height[start]
                start += 1
            else:
                tmp = (end-start) * height[end]
                end -= 1
            max_ = max(max_, tmp)
        return max_
