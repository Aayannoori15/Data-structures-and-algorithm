# 71. Simplify Path  [Medium]
# https://leetcode.com/problems/simplify-path/
# runtime 0 ms | memory 17.9 MB

class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        ans=[]
        final=[]
        path1=[]
        for i in path:
            if i!='':
                path1.append(i)
        path=path1
        for i in path:
            if i == '.':
                pass
            elif i == '..' :
                if ans:
                    ans.pop()
            elif i == '...' and len(ans)>1:
                ans.pop()
                ans.pop()
            else:
                ans.append(i)
        return '/' + '/'.join(ans) if ans else '/'
