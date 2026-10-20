# 283. Move Zeroes  [Easy]
# https://leetcode.com/problems/move-zeroes/
# runtime 3 ms | memory 18.8 MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
     j=0
     for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
     return nums
