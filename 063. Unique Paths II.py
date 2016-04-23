# -*- coding: utf-8 -*-
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
"""
# 62题的强化版.
# 从62题我们可以得出:Num(m,n) = Num(m-1,n) + Num(m,n-1)
# 并且这道题的关键点就是找出数组中两条边的值, 比如下面的数组
# [                          [
#   [0,0,0,0],                 [1,1,1,1]
#   [0,0,0,0],      ---->      [1,.....]
#   [0,0,0,0],      ---->      [1,.....]
#   [1,0,0,0]                  [0,.....]
# ]                          ]
# 只要得到原数组中第一排和第一列的节点的走法的数量,其他的点的走法可以全部推出
# 需要注意的是给出的数组中的点n的值为1时,我们得到的对应的结果应该是0




class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)       # 列
        n = len(obstacleGrid[0])    # 行
        _list = [[0 for i in range(n)] for j in range(m)]
        for pos, i in enumerate(obstacleGrid[0]):   # 第一排
            if i == 1:
                for j in range(pos):
                    _list[0][j] = 1
                break
            else:
                _list[0][pos] = 1

        for i in range(m):              # 第一列
            if obstacleGrid[i][0] == 1:
                for j in range(i):
                    _list[j][0] = 1
                break
            else:
                _list[i][0] = 1
        # print _list

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:     # 该点是障碍,不能到达
                    _list[i][j] = 0
                else:
                    _list[i][j] = _list[i-1][j] + _list[i][j-1] # 其他情况和62题一样
        # print _list
        return _list[m-1][n-1]

s = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [1,0,0,0]
]
s_ = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print Solution().uniquePathsWithObstacles(s_)

