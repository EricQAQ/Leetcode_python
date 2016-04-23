# -*- coding: utf-8 -*-
"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# 找出树的所有路径, 可以想到深度优先和广度优先遍历
# 深度优先遍历 -> 前序遍历 -> 递归 或者 栈
# 栈实现的时候,有个注意点:
# 由于需要输出路径,所以,压栈的时候除了压入节点,还需要压入当前的路径组成的字符串: (node, path),
# 但是使用递归的时候就不需要考虑这个.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    # 递归实现
    def dfs(self, root, path):
        if root.left is None and root.right is None:
            self._list.append(path)
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val))

    # 非递归实现, 栈
    def dfs_stack(self, stack):
        while len(stack) > 0:
            node, path = stack.pop()
            if not path:
                path += str(node.val)
            else:
                path = path + '->' + str(node.val)
            if node.left is None and node.right is None:
                self._list_stack.append(path)
            if node.right:
                stack.append((node.right, path))
            if node.left:
                stack.append((node.left, path))

    # 递归实现
    def binaryTreePaths(self, root):
        self._list = []
        if not root:
            return []
        self.dfs(root, str(root.val))
        return self._list

    # 非递归实现, 栈
    def binaryTreePaths_stack(self, root):
        if not root:
            return []
        self._list_stack = []
        stack = []
        stack.append((root, ''))
        self.dfs_stack(stack)
