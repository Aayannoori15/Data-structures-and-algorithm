# 1365. How Many Numbers Are Smaller Than the Current Number  [Easy]
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# runtime 31 ms | memory 17.9 MB

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy=nums.copy() 
        copy.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i] in copy:
                n=copy.index(nums[i])
                ans.append(n)
        return ans
