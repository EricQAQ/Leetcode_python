# -*- coding: utf-8 -*-
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def add_letter(pos, _list, string):
            if pos == len(digits):
                _list.append(string)
                return
            for item in dict[int(digits[pos])]:
                add_letter(pos+1, _list, string+item)

        dict = {
            0: ' ', 1: '*', 2: 'abc', 3: 'def', 4: 'ghi',
            5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        _list = []
        length = len(digits)
        if length == 0:
            return []
        add_letter(length, _list, '')
        return _list
