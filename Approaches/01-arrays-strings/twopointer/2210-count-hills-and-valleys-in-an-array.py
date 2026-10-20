# 2210. Count Hills and Valleys in an Array  [Easy]
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# runtime 0 ms | memory 17.7 MB

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a=0
        j=0
        for i in range (1,len(nums)-1):
            if((nums[j]<nums[i]>nums[i+1]) or (nums[j]>nums[i]<nums[i+1])):
                a+=1
                j=i
            else:
                continue
        return a
