# 1441. Build an Array With Stack Operations  [Medium]
# https://leetcode.com/problems/build-an-array-with-stack-operations/
# runtime 0 ms | memory 17.6 MB

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        target_set = set(target)
        for i in range(1,n+1):
            if i in target_set:
                stack.append('Push')
            else:
                stack.append('Push')
                stack.append('Pop')
            if i == target[-1]:
                break
        return stack
