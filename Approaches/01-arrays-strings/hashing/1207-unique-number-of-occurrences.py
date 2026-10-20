# 1207. Unique Number of Occurrences  [Easy]
# https://leetcode.com/problems/unique-number-of-occurrences/
# runtime 7 ms | memory 19.2 MB

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n=set(arr)
        sample=[]
        for i in n:
            sample.append(arr.count(i))
        sample.sort()
        for i in range(1,len(sample)):
            if sample[i]==sample[i-1]:
                return False 
        return True
