# 155. Min Stack  [Medium]
# https://leetcode.com/problems/min-stack/
# runtime 651 ms | memory 22.7 MB

class MinStack:

    def __init__(self):
        self.arr=[]

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        if not self.arr[-1] == None:
            return self.arr[-1]
        

    def getMin(self) -> int:
        mini=float('inf')
        for i in self.arr:
            if i<mini:
                mini=i
        return mini



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
