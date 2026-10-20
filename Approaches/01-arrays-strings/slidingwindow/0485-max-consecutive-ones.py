# 485. Max Consecutive Ones  [Easy]
# https://leetcode.com/problems/max-consecutive-ones/
# runtime 12 ms | memory 20.2 MB

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        cou=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                if count>=cou:
                    cou=count 
                count=0
        if count>cou:
            cou=count 
        return cou
