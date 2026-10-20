# 643. Maximum Average Subarray I  [Easy]
# https://leetcode.com/problems/maximum-average-subarray-i/
# runtime 54 ms | memory 27.4 MB
# local rewrite (cleaner than the submitted version)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
            
        return max_sum / k
