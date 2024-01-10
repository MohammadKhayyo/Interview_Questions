"""Add Two Numbers"""
"""Link to the problem: https://leetcode.com/problems/add-two-numbers/"""


class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(val=carry % 10)
            carry //= 10
            curr = curr.next

        return dummy.next
