# 151. Reverse Words in a String  [Medium]
# https://leetcode.com/problems/reverse-words-in-a-string/
# runtime 7 ms | memory 17.5 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.strip()
        a=a+' '
        ans=''
        word=''
        for i in a:
            if i!=' ':
                word+=i
            else:
                ans=word+' '+ans
                word=''
        ans=ans.strip()
        while '  ' in ans:
            ans = ans.replace('  ', ' ')
        return ans
