# 523. Continuous Subarray Sum  [Medium]
# https://leetcode.com/problems/continuous-subarray-sum/
# runtime 122 ms | memory 40.4 MB

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref=[0]
        for i in range(len(nums)):
            pref.append(pref[i]+nums[i])
        for i in range(len(pref)):
            pref[i]=pref[i]%k
        dictionary = {}
        for idx in range(len(pref)):
            if pref[idx] in dictionary:
                if idx-dictionary[pref[idx]]>1:
                    return True 
            else:
                dictionary[pref[idx]] = idx 
        return False
