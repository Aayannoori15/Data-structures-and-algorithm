# 287. Find the Duplicate Number  [Medium]
# https://leetcode.com/problems/find-the-duplicate-number/
# runtime 31 ms | memory 33.4 MB

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=0
        f=0
        while True:
            if s == f and s!=0:
                break
            else:
                s = nums[s]      
                f = nums[nums[f]]
        s=0
        while s!=f:
                s = nums[s]      
                f = nums[f]
        return s
