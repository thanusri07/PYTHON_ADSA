#Implementation of  Circular Queue 
class Circular_Queue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * self.size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, val):
        #Queue is full
        if self.front == (self.rear + 1) % self.size:
            return "Queue is full"
        #Queue is empty
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = val
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        val = self.q[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val
q=Circular_Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
#leetcode: 20
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

#leetcode:232
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x: int) -> None:
        self.stack_in.append(x)
    def pop(self) -> int:
        self.move_elements()
        return self.stack_out.pop()
    def peek(self) -> int:
        self.move_elements()
        return self.stack_out[-1]
    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
    def move_elements(self) -> None:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
