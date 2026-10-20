# 977. Squares of a Sorted Array  [Easy]
# https://leetcode.com/problems/squares-of-a-sorted-array/
# runtime 2 ms | memory 21 MB

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new =[x*x for x in nums]
        return sorted(new)
