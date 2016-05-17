# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        _dict = {}
        max_len = 0
        start = 0

        for pos, item in enumerate(s):
            if item in _dict:
                start = max(start, _dict[item]+1)
            _dict[item] = pos

            max_len = max(max_len, pos-start+1)
        return max_len
