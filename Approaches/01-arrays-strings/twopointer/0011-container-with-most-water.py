# 11. Container With Most Water  [Medium]
# https://leetcode.com/problems/container-with-most-water/
# runtime 35 ms | memory 29.9 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxi=0
        while i<j:
            val=0
            if height[i]>=height[j]:
                val=height[j]*(j-i)
                j-=1
                if val>maxi:
                    maxi=val
            elif height[j]>=height[i]:
                val=height[i]*(j-i)
                i+=1
                if val>maxi:
                    maxi=val
        return maxi
