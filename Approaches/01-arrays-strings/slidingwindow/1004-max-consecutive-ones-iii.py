# 1004. Max Consecutive Ones III  [Medium]
# https://leetcode.com/problems/max-consecutive-ones-iii/
# runtime 63 ms | memory 22.2 MB

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=zeros=max_c=0
        for r in range(len(nums)) :
            if nums[r]==0:
                    zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            w=r-l+1
            max_c=max(max_c,w)
        return max_c
