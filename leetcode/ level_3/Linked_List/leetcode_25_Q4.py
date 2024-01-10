"""Reverse Nodes in k-Group"""
"""Link to the problem: https://leetcode.com/problems/reverse-nodes-in-k-group/"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data, self.head)
        self.head = new_node

    def printList(self, head=None):
        temp = head
        while temp:
            print('%d->' % temp.val, end="")
            temp = temp.next
        print("NULL")

    def reverseKGroup(self, head, k: int):
        temp = head
        if not temp or k == 1:
            return temp

        def getLength(temp: ListNode) -> int:
            _temp = temp
            length = 0
            while _temp:
                length += 1
                _temp = _temp.next
            return length

        length = getLength(temp)
        dummy = ListNode(0, temp)
        prev = dummy
        curr = temp

        for _ in range(length // k):
            for _ in range(k - 1):
                _next = curr.next
                curr.next = _next.next
                _next.next = prev.next
                prev.next = _next
            prev = curr
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    llist = Solution()
    n = 5
    k = 2
    for i in range(n, 0, -1):
        llist.push(i)
    llist.printList(llist.head)
    llist.head = llist.reverseKGroup(llist.head, k)
    llist.printList(llist.head)
