# 238. Product of Array Except Self  [Medium]
# https://leetcode.com/problems/product-of-array-except-self/
# runtime 15 ms | memory 23 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z=nums.count(0)
        prod=1
        new=[]
        for i in nums:
            if z==0:
                prod*=i
            elif z==1:
                if i == 0:
                    continue
                else:
                    prod*=i
        for i in nums:
            if z ==0:
                new.append(prod//i)
            elif z==1:
                if i==0:
                    new.append(prod)
                else:
                    new.append(0)
            else:
                 new.append(0)
        return new
