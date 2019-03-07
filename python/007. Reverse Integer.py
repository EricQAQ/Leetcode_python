# -*- coding: utf-8 -*-
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True
        if x < 0:
            flag = False
        x = str(abs(x))
        x = int(x[::-1])
        if x > 2147483647:
            return 0
        if flag:
            return x
        return -x
