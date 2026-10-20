# 724. Find Pivot Index  [Easy]
# https://leetcode.com/problems/find-pivot-index/
# runtime 8 ms | memory 18.8 MB

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=sum(nums)
        left=0
        b=-1
        for i in range(len(nums)):
            if i!=0:
                left+=nums[i-1]
            if left!=(a-nums[i]-left):
                continue
            else:
                b=i
                break
        return b
