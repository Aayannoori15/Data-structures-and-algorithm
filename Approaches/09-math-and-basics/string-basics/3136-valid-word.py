# 3136. Valid Word  [Easy]
# https://leetcode.com/problems/valid-word/
# runtime 0 ms | memory 17.9 MB

class Solution:
    def isValid(self, word: str) -> bool:
        a=0
        b=0
        if len(word)<3:
            return False
        nig="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        vowels="AEIOUaeiou"
        consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
        for i in word:
            if i in nig:
                continue
            else:
                return False
        for i in word:
            if i in vowels:
                a+=1
        for i in word:
            if i in consonants:
                b+=1
        if a>0 and b>0:
            return True
        return False
