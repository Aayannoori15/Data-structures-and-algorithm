# 35. Search Insert Position  [Easy]
# https://leetcode.com/problems/search-insert-position/
# runtime 0 ms | memory 18.5 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
