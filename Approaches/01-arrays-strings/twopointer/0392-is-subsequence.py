# 392. Is Subsequence  [Easy]
# https://leetcode.com/problems/is-subsequence/
# runtime 0 ms | memory 18 MB

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        a=""
        while j<len(t) and i<len(s):
            if t[j]==s[i]:
                a+=t[j]
                i+=1 
            j+=1
        return s==a
