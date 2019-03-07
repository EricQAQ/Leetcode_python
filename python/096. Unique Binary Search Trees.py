# -*- coding: utf-8 -*-
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# 二叉搜索树的特点是对于节点n来说,n的左子树所有节点都小于n, 右子树都大于n
# 本题中n个点中每个点都可以作为root:
# 当i作为root时,小于i的点都只能放在其左子树中,大于i的点只能放在右子树中,
# 此时只需求出左、右子树各有多少种,二者相乘即为以i作为root时BST的总数。
# 注意求出来的值只是当i为根的二叉搜索树的个数,所以要求和才是n个节点可以组成的二叉搜索树的总的个数...
# 所以该问题化简为以i为根，其唯一左子树和右子树各有多少，这就是个动态规划的问题了


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        _list = [1, 1, 2]
        _list.extend([0 for i in range(n-2)])
        if n < 3:
            return _list[n]
        for i in range(3, n+1):
            for j in range(i):
                _list[i] += _list[j] * _list[i-j-1]
        return _list[n]
