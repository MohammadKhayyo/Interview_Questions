"""Reorder List"""
"""Link to the problem: https://leetcode.com/problems/reorder-list/"""

from typing import (
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
        # Utility function to print the LinkedList

    def printList(self):
        temp = self.head
        while temp:
            print('%d->' % temp.val, end="")
            temp = temp.next
        print("NULL")

    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head


if __name__ == "__main__":

    llist = Solution()
    for i in range(5, 0, -1):
        llist.push(i)

    print("Given Linked List")
    llist.printList()

    llist.head = llist.reorderList(llist.head)
    llist.printList()
