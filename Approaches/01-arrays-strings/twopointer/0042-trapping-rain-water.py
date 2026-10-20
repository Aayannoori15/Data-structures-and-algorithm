# 42. Trapping Rain Water  [Hard]
# https://leetcode.com/problems/trapping-rain-water/
# runtime 254 ms | memory 21 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=[]
        rmax=[]
        m=0
        for i in range(len(height)):
            m=max(m,height[i])
            lmax.append(m)
        m=0
        for i in range(-1,-len(height)-1,-1):
            m=max(m,height[i])
            rmax.insert(0, m)
        ans=0
        for i in range(len(height)):
            left=lmax[i]
            right=rmax[i]
            quant=min(left,right)-height[i]
            if quant>0:
                ans+=quant 
        return ans
