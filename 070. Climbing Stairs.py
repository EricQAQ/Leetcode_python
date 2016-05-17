# -*- coding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?
"""
# 找规律可以发现: 第n阶的走法 = 第n-1阶的走法 + 第n-2阶的走法
# 下面先用了递归的解法(climb函数),但是超时,所以改用更简单粗暴的算法


class Solution(object):
    def climb(self, n):
        if n <= 0:
            return 0
        elif n <= 3:
            return n
        self.total = self.climb(n-1) + self.climb(n-2)
        return self.total

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # self.total = 0
        # return self.climb(n)
        if n <= 0:
            return 0
        elif n <= 3:
            return n
        count = 3
        value = [2, 3]
        while count < n:
            value = [value[1], value[0]+value[1]]
            count += 1
        return value[1]


print Solution().climbStairs(1)
