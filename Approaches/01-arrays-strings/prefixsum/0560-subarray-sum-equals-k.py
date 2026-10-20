# 560. Subarray Sum Equals K  [Medium]
# https://leetcode.com/problems/subarray-sum-equals-k/
# runtime 31 ms | memory 22.2 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=[0]
        for i in range(len(nums)):
            pref.append(pref[i]+nums[i])
        dictionary={}
        ans=0
        for i in pref:
            
            if i-k in dictionary:
                ans+=dictionary[i-k]
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1

        return ans
