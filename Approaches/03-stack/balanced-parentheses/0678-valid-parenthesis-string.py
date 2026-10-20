# 678. Valid Parenthesis String  [Medium]
# https://leetcode.com/problems/valid-parenthesis-string/
# runtime 0 ms | memory 19.5 MB

class Solution:
    def checkValidString(self, s: str) -> bool:
        star=[]
        ind=[]
        for i in range(len(s)):
            if s[i] == '(':
                ind.append(i)
            elif s[i] == ')':
                if len(ind)!=0:
                    ind.pop(-1)
                elif len(star) != 0:
                    star.pop(-1)
                else :
                    return False
            elif s[i]=='*':
                star.append(i)
        while ind and star:
            if star[-1]>ind[-1]:
                ind.pop()
                star.pop()
            else:
                return False
        return len(ind)==0
