# -*- coding: utf-8 -*-
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# 本题使用了一个特殊的解法:把所有节点放入list中,然后进行列表操作
# 另一个解法是使用双指针:
# 第一个指针从head开始遍历,当遍历到第n个节点的时候, 第二个指针开始从head遍历
# 这样, 当第一个指针到链表尾部的时候, 第二个指针正好到达倒数第n个节点


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        nodes = []
        root = head

        while root:
            nodes.append(root)
            root = root.next
        if n == len(nodes):
            return head.next
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[len(nodes)-n-1].next = nodes[len(nodes)-n+1]
        return nodes[0]

