"""Remove Nth Node From End of List"""
"""Link to the problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/"""
from typing import (
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Function to initialize head
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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        if n > 0:
            return head

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


if __name__ == "__main__":
    llist = Solution()
    # for i in range(5, 0, -1):
    #     llist.push(i)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Given Linked List")
    llist.printList()

    llist.head = llist.removeNthFromEnd(llist.head, 3)
    llist.printList()
