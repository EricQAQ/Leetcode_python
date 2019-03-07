# -*- coding: utf-8 -*-
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX

        if (dividend < 0 and divisor < 0) or (dividend >0 and divisor > 0):
            flag = True
        else:
            flag = False
        divisor = abs(divisor)
        dividend = abs(dividend)

        value = 0
        count_shift = 31

        while count_shift >= 0:
            if dividend >= divisor << count_shift:
                dividend -= divisor << count_shift
                value += 1 << count_shift
            count_shift -= 1

        if not flag:
            value = -value
        if value > INT_MAX:
            return INT_MAX
        return value

print Solution().divide(10, 3)

