# 643. Maximum Average Subarray I  [Easy]
# https://leetcode.com/problems/maximum-average-subarray-i/
# runtime 54 ms | memory 27.4 MB

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a=sum(nums[0:k])
        temp=a
        for i in range(len(nums)-k):
            if a-nums[i]+nums[i+k]>temp:
                temp=a-nums[i]+nums[i+k]
                a=a-nums[i]+nums[i+k]
            else:
                a=a-nums[i]+nums[i+k]
        return temp/k
