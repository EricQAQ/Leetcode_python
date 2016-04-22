# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
"""
# 中序遍历. 左子树 -> 本节点 -> 右子树
# 基本上有两种解法,第一种:递归, 第二种:通过栈的方式


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归解法
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, _list):
            if root:
                inorder(root.left, _list)
                _list.append(root.val)
                inorder(root.right, _list)
        _list = []
        inorder(root, _list)
        return _list


# 非递归解法, 使用栈解决
# 总体入栈顺序是: 右子树 -> 本节点 -> 左子树
# 下面的方法同样适用于前序,后序
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        _list = []
        stack.append((root, 0))     # 0: 未访问, 1: 访问过

        while len(stack) > 0:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                _list.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))

        return _list
