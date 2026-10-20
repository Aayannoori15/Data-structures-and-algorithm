# 26. Remove Duplicates from Sorted Array  [Easy]
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# runtime 23 ms | memory 20.5 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new=[]
        for i in nums:
            if i not in new:
                new.append(i)
        nums[:] = new
