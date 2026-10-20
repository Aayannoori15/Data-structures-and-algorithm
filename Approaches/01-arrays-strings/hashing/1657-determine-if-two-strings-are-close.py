# 1657. Determine if Two Strings Are Close  [Medium]
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# runtime 227 ms | memory 21.6 MB

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1=list(word1)
        word2=list(word2)
        if len(word1)!=len(word2):
            return False
        word1.sort()
        word2.sort()
        if word1==word2:
            return True 
        if set(word1)!=set(word2):
            return False 
        dict1={}
        dict2={}
        for i in word1:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in word2:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        return sorted(dict1.values()) == sorted(dict2.values())
