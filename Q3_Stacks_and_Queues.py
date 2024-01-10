# 3. Stacks and Queues:
from _collections import deque


# • Implement a stack using two queues.
class Stack:

    def __init__(self):

        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

        # Push x first in empty q2
        self.q2.append(x)

        # Push all the remaining
        # elements in q1 to q2.
        while self.q1:
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def top(self):
        if self.q1:
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)

    def empty(self):
        return self.size() == 0


# • Implement a queue using two stacks.
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def empty(self):
        return len(self.s1) == 0

    def enQueue(self, x):

        # Move all elements from s1 to s2
        while not self.empty():
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into self.s1
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    # Dequeue an item from the queue
    def deQueue(self):

        # if first stack is empty
        if self.empty():
            return -1

        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x

    def front(self):
        if self.empty():
            return -1
        x = self.s1[-1]
        return x

    def rear(self):
        if self.empty():
            return -1
        x = self.s1[0]
        return x


# • Write a program to check if a given string of parentheses is balanced.
def is_balanced_parentheses(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if stack and open_list[pos] == stack[-1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == "__main__":
    # 3. Stacks and Queues:
    # • Implement a stack using two queues.
    s = Stack()
    print("is empty ? ", s.empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    print("current size: ", s.size())
    print("is empty ? ", s.empty())

    # • Implement a queue using two stacks.
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print("is empty ? ", q.empty())
    # • Write a program to check if a given string of parentheses is balanced.
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    string = "{[]{()}}"
    print(string, "-", is_balanced_parentheses(string))
    string = "[{}{})(]"
    print(string, "-", is_balanced_parentheses(string))
    string = "((()"
    print(string, "-", is_balanced_parentheses(string))
    string = ")"
    print(string, "-", is_balanced_parentheses(string))
