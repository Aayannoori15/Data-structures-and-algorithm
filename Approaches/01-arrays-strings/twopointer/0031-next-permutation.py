# 31. Next Permutation  [Medium]
# https://leetcode.com/problems/next-permutation/
# runtime 0 ms | memory 19.3 MB

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p=len(nums)-2
        
        while p>=0:
            if nums[p+1]<=nums[p]:
                p-=1
            else:
                break
        if p==-1:
            nums[p+1:] = sorted(nums[p+1:])
            return
        
        for i in range(len(nums)-1, p, -1):
            if nums[i] > nums[p]:
                nums[i], nums[p] = nums[p], nums[i]
                nums[p+1:] = reversed(nums[p+1:])
                break
