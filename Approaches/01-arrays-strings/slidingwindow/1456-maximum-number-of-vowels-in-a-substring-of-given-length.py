# 1456. Maximum Number of Vowels in a Substring of Given Length  [Medium]
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# runtime 67 ms | memory 18 MB

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=list('aeiou')
        a=0
        for i in s[0:k]:
            if i in vowels:
                a+=1
        temp=a
        for i in range(0,len(s)-k):
            if s[i] in vowels:
                a-=1
            if s[i+k] in vowels:
                a+=1
            if a>temp:
                temp=a
        return temp
