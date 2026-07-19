class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=len(nums)
        i=0
        j=1
        r=[]
        while i < j < a:
            if nums[i]+nums[j]==target :
                r=[i,j]
                break
            else :
                j+=1
            if j==a:
                i+=1
                j=i+1
        return r