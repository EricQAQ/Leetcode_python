# -*- coding: utf-8 -*-
"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
# 可以找到规律: Num(m,n) = Num(m-1,n) + Num(m,n-1)
# 递归方法会超时, 改用二维数组实现


class Solution(object):
    # 递归方法,超时
    def move(self, m, n):
        if m <= 0 or n <= 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        self.total = self.move(m-1, n) + self.move(m, n-1)
        return self.total

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 递归方法,超时
        # return self.move(m, n)

        # 非递归方法
        if m == 0 or n == 0:
            return 0
        _list = [[1 for i in range(n)] for j in range(m)]
        count_m = count_n = 1
        while count_m < m:
            while count_n < n:
                _list[count_m][count_n] = \
                    _list[count_m-1][count_n] + _list[count_m][count_n-1]
                count_n += 1
            count_n = 1
            count_m += 1
        return _list[m-1][n-1]

        # 下面的方法和上面的一样,只是换了个表示方法
        # path = [[1 for j in range(n)] for i in range(m)]
        #
        # if m == 0 or n == 0:
        #     return 0
        # for i in range(1, m):
        #     for j in range(1, n):
        #         path[i][j] = path[i-1][j] + path[i][j-1]
        # return path[m-1][n-1]


print Solution().uniquePaths(3, 3)
