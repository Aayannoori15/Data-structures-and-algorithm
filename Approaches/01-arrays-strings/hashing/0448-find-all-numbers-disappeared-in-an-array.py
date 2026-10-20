# 448. Find All Numbers Disappeared in an Array  [Easy]
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# runtime 68 ms | memory 40.5 MB

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums1=[]
        ans=[]
        for i in range(1,len(nums)+1):
            nums1.append(i)
        nums=set(nums)
        nums1=set(nums1)
        ans =nums1-nums
        return list(ans)
