# 232. Implement Queue using Stacks  [Easy]
# https://leetcode.com/problems/implement-queue-using-stacks/
# runtime 0 ms | memory 19.6 MB

class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for i in range (len(self.stack1)):
            n=self.stack1[0]
            if i!=0:
                self.stack2.append(self.stack1[i])
        self.stack1=self.stack2
        self.stack2=[]
        return n

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
