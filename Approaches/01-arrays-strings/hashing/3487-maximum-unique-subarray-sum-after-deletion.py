# 3487. Maximum Unique Subarray Sum After Deletion  [Easy]
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
# runtime 0 ms | memory 17.8 MB

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums=set(nums)
        a=0
        if len(nums) ==1 :
            return list(nums)[0]
        else :
           for i in nums:
            if i>=0 :
               a+=i
            else:
              continue
        if a == 0:
                a = max(nums)

        return a
