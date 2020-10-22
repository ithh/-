#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
File    :   2.py
Time    :   2020/10/22 14:06:08
Author  :   ithh 
Version :   1.0
Contact :   hhxhwxh@qq.com
Desc    :   None
'''
'''
给出两个非空的链表用来表示两个非负的整数。其中它们各自的位数是按照逆序的方式存储的，
并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外这两个数都不会以0开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0) # 哨兵
        cur = res # 游标
        carry = 0 # 进位数
        while l1 or l2 or carry:
            residual1 = l1.val if l1 else 0
            residual2 = l2.val if l2 else 0
            cur.next = ListNode((residual1+residual2+carry) % 10)
            carry = (residual1 + residual2 + carry) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return res.next
