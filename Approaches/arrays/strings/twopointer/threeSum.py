class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()
        
        for j in range(1, len(nums) - 1):
            seen=set(nums[j+1:])
            for i in range(0, j):
                third = -(nums[i] + nums[j])
                if third in seen:
                    triplet = (nums[i], nums[j], third) 
                    result.add(triplet)
        
        return [list(t) for t in result]