# 2390. Removing Stars From a String  [Medium]
# https://leetcode.com/problems/removing-stars-from-a-string/
# runtime 219 ms | memory 20.2 MB

class Solution:
    def removeStars(self, s: str) -> str:
        s=list(s)
        i=0
        ans=[]
        while i<len(s):
            if s[i]!='*':
                ans.append(s[i])
            else:
                ans.pop()
            i+=1
        ans=''.join(ans)
        return ans
