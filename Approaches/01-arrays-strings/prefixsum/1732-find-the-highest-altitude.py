# 1732. Find the Highest Altitude  [Easy]
# https://leetcode.com/problems/find-the-highest-altitude/
# runtime 0 ms | memory 17.7 MB

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result=[0]
        i=0
        j=0
        max=0
        while i < len(gain) and j <len(gain):
           net=result[j]+gain[i]
           result.append(net)
           i+=1
           j+=1
        for i in result:
            if i>max:
                max=i
        return max
