# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# 判断给定的二叉树是否是二叉搜索树
# 二叉搜索树的特点是:某节点的左子树的值都比该节点小,右子树的值都比该节点大.(注意是整个子树的所有节点的值)
# 二叉搜索树有个特点: 中序遍历所得到的数组一定是一个递增数组!
# 后面大家都懂的


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root, _list):
            if root:
                inorder(root.left, _list)
                _list.append(root.val)
                inorder(root.right, _list)
        _list = []
        inorder(root, _list)
        count = 0
        while count < len(_list)-1:
            if _list[count] >= _list[count+1]:
                return False
        return True



