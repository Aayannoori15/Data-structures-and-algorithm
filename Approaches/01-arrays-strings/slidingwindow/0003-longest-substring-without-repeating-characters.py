# 3. Longest Substring Without Repeating Characters  [Medium]
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# runtime 218 ms | memory 20.2 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        seen=set()
        i=0
        j=0
        while j<len(s):
            if s[j] in seen:
                while s[i]!=s[j]:
                    seen.remove(s[i])
                    i+=1
                seen.remove(s[i])
                i+=1
                seen.add(s[j])
            else:
                seen.add(s[j])
            if j-i+1>=maxx:
                maxx=j-i+1
            j+=1

        return maxx
