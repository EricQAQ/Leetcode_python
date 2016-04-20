# -*- coding: utf-8 -*-
"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
# 可以直接使用str的函数find,返回值:
# return haystack.find(needle)


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        elif haystack == '' and needle != '':
            return -1

        j = 0
        i = 0
        while i < len(haystack):
            # print i, j, haystack[i], needle[j]
            if haystack[i] == needle[j] and j < len(needle)-1:
                j += 1
                i += 1
            elif haystack[i] == needle[j] and j == len(needle)-1:
                return i-j
            elif haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
        return -1
