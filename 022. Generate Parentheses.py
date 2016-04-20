# -*- coding: utf-8 -*-
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
# 递归.
# 可以发现, 左括号需要有n个,右括号需要有n个, 所以需要判断左右括号和n的大小
# 当左括号个数n_L > 右括号个数n_R的时候,可以插入右括号


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(_list, string, count, left, right):
            if left > count or right > count:
                return
            if left == right and left == count:
                _list.append(string)
                return
            generate(_list, string+'(', count, left+1, right)
            if left > right:
                generate(_list, string+')', count, left, right+1)

        _list = []

        generate(_list, '', n, 0, 0)

        return _list

print Solution().generateParenthesis(4)
