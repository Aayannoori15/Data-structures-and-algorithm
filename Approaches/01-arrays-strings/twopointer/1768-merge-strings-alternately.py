# 1768. Merge Strings Alternately  [Easy]
# https://leetcode.com/problems/merge-strings-alternately/
# runtime 48 ms | memory 17.9 MB

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i=0
        if len(word1) >  len(word2):
            while i < len(word2):
                s=s+word1[i]+word2[i]
                i+=1
            s=s+word1[len(word2):len(word1)+1]
        elif len(word2) >  len(word1):
            while i < len(word1):
                s=s+word1[i]+word2[i]
                i+=1
            s=s+word2[len(word1):len(word2)+1]
        elif len(word1)==len(word2):
            while i < len(word1):
                s=s+word1[i]+word2[i]
                i+=1
        return s
