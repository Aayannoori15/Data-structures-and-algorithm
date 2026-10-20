# 1791. Find Center of Star Graph  [Easy]
# https://leetcode.com/problems/find-center-of-star-graph/
# runtime 0 ms | memory 43.4 MB

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s1=None 
        s2=None
        for u,v in edges:
            if not s1:
                s1=u
                s2=v
            else:
                if u==s1:
                    return u
                elif u==s2:
                    return u
                elif v==s1:
                    return v
                elif v==s2:
                    return v
