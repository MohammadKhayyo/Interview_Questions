# 2. Linked Lists:
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to reverse the linked list
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def reverseListRecursive(self):
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                nxt = cur.next
                cur.next = prev
                return reverse(nxt, cur)

        self.head = reverse(self.head, None)

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print('%d->' % temp.data, end="")
            temp = temp.next
        print("NULL")

    def getLen(self):
        temp = self.head
        _len = 0

        while temp:
            _len += 1
            temp = temp.next

        return _len

    def findMiddle(self):
        if self.head:
            # find length
            _len = self.getLen()
            temp = self.head

            # traverse till we reached half of length
            midIdx = _len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1

            return temp.data

    def detectLoop(self):
        """
        Detect if a linked list has a cycle using Floyd's Cycle-Finding Algorithm.
        """
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Function to make loop at k-th elements of linked list
    def makeLoop(self, k):
        # traverse the linked list until loop
        # point not found
        temp = self.head
        count = 1
        while count < k:
            temp = temp.next
            count = count + 1

        # backup the joint point
        joint_point = temp

        # traverse remaining nodes
        while temp.next:
            temp = temp.next

        # joint the last node to k-th element
        temp.next = joint_point
        return self.head


if __name__ == "__main__":
    # 2. Linked Lists:
    # • Write a program to reverse a linked list.
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    print("Given Linked List")
    llist.printList()
    llist.reverse()
    print("Reversed Linked List")
    llist.printList()

    llist.reverseListRecursive()
    print("Reversed Linked List - Recursive")
    llist.printList()

    # • Write a program to find the middle element of a linked list.
    mid = llist.findMiddle()
    print('The middle element is: ', mid)
    print(llist.detectLoop())
    # MAKE Loop
    len_llist = llist.getLen()
    llist.makeLoop(len_llist // 2)
    print(llist.detectLoop())
