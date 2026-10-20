# 1456. Maximum Number of Vowels in a Substring of Given Length  [Medium]
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# runtime 67 ms | memory 18 MB
# local rewrite (cleaner than the submitted version)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx = float('-inf')
        seen = set("aeiou")
        vw = 0 
        l = 0 
        for i in range(len(s)):
            if s[i] in seen:
                vw += 1
            
            if i - l+ 1 == k:
                mx = max(mx,vw)
               
                if s[l] in seen:
                    vw -= 1
                l += 1
        return mx 
