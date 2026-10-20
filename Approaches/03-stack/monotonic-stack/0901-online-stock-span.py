# 901. Online Stock Span  [Medium]
# https://leetcode.com/problems/online-stock-span/
# runtime 73 ms | memory 24 MB

class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.span=0

    def next(self, price: int) -> int:
        self.span+=1
        if not self.stack:
            self.stack.append([price,self.span])
            return self.span
        elif self.stack and price<self.stack[-1][0]:
            ans=self.span-self.stack[-1][1]
            self.stack.append([price,self.span])
            return ans
        else:
            while self.stack and price>=self.stack[-1][0]:
                self.stack.pop()
            if self.stack:
                ans=self.span-self.stack[-1][1]
            else:
                self.stack.append([price,self.span])
                return self.span
        self.stack.append([price,self.span])
        return ans
