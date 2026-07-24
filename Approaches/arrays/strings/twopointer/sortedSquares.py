class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        i=0
        j=len(nums)-1
        if i==j:
            return [nums[i]*nums[i]]
        while i<j:
            nums[i]=nums[i]*nums[i]
            nums[j]=nums[j]*nums[j]
            i+=1
            j-=1
        if i==j:
            nums[i]=nums[i]*nums[i]
        return sorted(nums)
        
            