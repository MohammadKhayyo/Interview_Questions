"""Merge Two Sorted Lists"""
"""Link to the problem: https://leetcode.com/problems/merge-two-sorted-lists/"""
from typing import (
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Recursive"""

    # def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    #     if list1 is None:
    #         return list2
    #     if list2 is None:
    #         return list1
    #
    #     if list1.val < list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2

    def printList(self, node):
        temp = node
        while temp.next is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print(temp.val)

    """iteration"""

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


if __name__ == '__main__':
    solution = Solution()

    llist1 = ListNode(1)
    llist1.next = ListNode(2)
    llist1.next.next = ListNode(4)

    llist2 = ListNode(1)
    llist2.next = ListNode(3)
    llist2.next.next = ListNode(4)
    Input = {"list1": llist1, "list2": llist2}
    print("Input:")
    print("list1:")
    solution.printList(llist1)
    print("list2:")
    solution.printList(llist2)
    Output = solution.mergeTwoLists(Input["list1"], Input["list2"])
    print("Output:")
    solution.printList(Output)
