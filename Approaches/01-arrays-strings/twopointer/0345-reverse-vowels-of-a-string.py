# 345. Reverse Vowels of a String  [Easy]
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# runtime 15 ms | memory 18.6 MB

class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        vowels=['a', 'e', 'i', 'o', 'u', 'A' , 'E', 'I', 'O','U']
        while i<j:
            if s[i] in vowels:
                if s[j] in vowels:
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                 i+=1
        return ''.join(s)
