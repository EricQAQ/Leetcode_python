# -*- coding: utf-8 -*-
"""
Implement pow(x, n).
"""
# 手动实现幂乘
# 最基础的做法是一个一个乘,这样比较慢. 所以可以进阶一下:以x*x为底数
# 这样每乘一次, 平方数需要除以二. 当平方数为奇数的时候需要注意一下

# 几个特殊点:
# 1. 注意x和n的正负值: x<0 and n是奇数, 则返回值应该为负数, 其他情况是正数
# 2. 注意n=0的情况
# 3. 注意n<0的情况


class Solution(object):
    def pow(self, x, n):
        if n < 0:
            x = 1/float(x)
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        base = x * x
        if n % 2 == 1:
            return x * self.pow(base, n/2)
        else:
            return self.pow(base, n/2)

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = False if x < 0 and n % 2 == 1 else True
        value = self.pow(abs(x), n)
        if flag:
            return value
        else:
            return -value


print Solution().myPow(-13.62608,3)
