# 20. Valid Parentheses  [Easy]
# https://leetcode.com/problems/valid-parentheses/
# runtime 0 ms | memory 18 MB

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False 
        ans=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in '([{' and i != len(s)-1:
                ans.append(s[i])
            elif s[i]=='}':
                if len(ans) !=0 and ans[-1]=='{':
                    ans.pop()
                else :
                    return False
            elif s[i]==']':
                if len(ans) !=0 and ans[-1]=='[':
                    ans.pop()
                else :
                    return False
            elif s[i]==')':
                if len(ans) !=0 and ans[-1]=='(':
                    ans.pop()
                else :
                    return False
            
        return len(ans)==0
