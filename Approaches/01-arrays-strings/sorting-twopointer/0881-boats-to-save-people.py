# 881. Boats to Save People  [Medium]
# https://leetcode.com/problems/boats-to-save-people/
# runtime 48 ms | memory 25 MB

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        nig=[]
        while j>=i:
            if people[i]+people[j]<=limit:
                nig.append(0)
                i+=1
                j-=1
            elif people[i]+people[j]>limit:
                nig.append(0)
                j-=1

        return len(nig)
