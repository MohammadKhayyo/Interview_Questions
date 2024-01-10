"""Reverse Linked List"""
"""Link to the problem: https://leetcode.com/problems/reverse-linked-list/"""
from typing import (
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""in file Q2_Linked_Lists.py"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverseListRecursive(self, head):
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                nxt = cur.next
                cur.next = prev
                return reverse(nxt, cur)

        return reverse(head, None)
