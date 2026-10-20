# 443. String Compression  [Medium]
# https://leetcode.com/problems/string-compression/
# runtime 3 ms | memory 17.9 MB

class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        i=1
        count=1
        while i < len(chars):
            if chars[i]==chars[i-1]:
                count+=1
                i+=1
            else:
                s+=chars[i-1]
                if count>1:
                   s+=str(count)
                count=1
                i+=1
        s+=chars[-1]
        if count>1:
            s+=str(count)
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)
