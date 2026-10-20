# 739. Daily Temperatures  [Medium]
# https://leetcode.com/problems/daily-temperatures/
# runtime 112 ms | memory 35.1 MB

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]> stack[-1][0]:
                temp, index = stack.pop()
                ans[index] = i - index
            stack.append((temperatures[i], i))
        return ans
