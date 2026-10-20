# 4. Median of Two Sorted Arrays  [Hard]
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# runtime 2 ms | memory 18.2 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        x = len(nums3)
        
        if x % 2 == 0:
            a = nums3[x // 2 - 1]
            b = nums3[x // 2]
            return (a + b) / 2
        else:
            return float(nums3[x // 2])
