# 1493. Longest Subarray of 1's After Deleting One Element  [Medium]
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# runtime 58 ms | memory 24.4 MB

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=1
        max_size=0
        dummy=0
        idx=float('inf')
        i=0
        if 0 not in nums:
            return len(nums)-1
        while i<(len(nums)):
            if nums[i] == 0 and count == 1:
                count-=1
                idx=i+1
                i+=1
            elif nums[i] == 0 and count == 0:
                if max_size<dummy:
                    max_size=dummy 
                i=idx
                count=1
                dummy=0
            elif nums[i]==1:
                dummy+=1
                i+=1
        return max(max_size, dummy)
