# 645. Set Mismatch  [Easy]
# https://leetcode.com/problems/set-mismatch/
# runtime 3371 ms | memory 19.2 MB

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
        for i in range(1,len(nums)+1):
            if i in nums:
                pass
            else:
                ans.append(i)
        return ans
