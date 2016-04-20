# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
# 日常——栈的使用
# 写过计算器的都明白的


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for letter in s:
            if letter not in ('(', ')', '{', '}', '[', ']'):
                return False
            elif letter in ('(', '{', '['):
                stack.append(letter)
            elif letter in (')', '}', ']') and len(stack) > 0:
                tmp = stack.pop()
                if (letter, tmp) not in (('(', ')'), ('{', '}'), ('[', ']')):
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False

