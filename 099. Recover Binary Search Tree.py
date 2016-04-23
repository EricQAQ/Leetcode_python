# -*- coding: utf-8 -*-
"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
# 关键点: 利用中序遍历二叉搜索树可以得到一个递增数组的特点
# 空间复杂度为常数空间的解决办法的关键是: 保证当前节点的值>前一节点的值
# 使用一个变量来存储前一节点


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if self.prev and self.prev.val > root.val:
                if not self.n1:
                    self.n1 = self.prev
                    self.n2 = root
                else:
                    self.n2 = root
            self.prev = root
            self.inorder(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = self.n1 = self.n2 = None
        self.inorder(root)

        tmp = self.n1.val
        self.n1.val = self.n2.val
        self.n2.val = tmp


n1 = TreeNode(0)
n2 = TreeNode(1)
n1.left = n2
Solution().recoverTree(n1)
print n1.val

