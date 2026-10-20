# 1470. Shuffle the Array  [Easy]
# https://leetcode.com/problems/shuffle-the-array/
# runtime 60 ms | memory 18.1 MB

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
        return ans
