# 649. Dota2 Senate  [Medium]
# https://leetcode.com/problems/dota2-senate/
# runtime 67 ms | memory 18.2 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        r=[]
        d=[]
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=='R':
                r.append(i)
            elif senate[i]=='D':
                d.append(i)
        while r and d:
            if r[0]<d[0]:
                d.pop(0)
                r.append(r.pop(0)+n)
            elif r[0]>d[0]:
                r.pop(0)
                d.append(d.pop(0)+n)
        if len(r)==0:
                return 'Dire'
        if len(d)==0:
                return 'Radiant'
